
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MovieRatingSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Rating System")

        self.movie_ratings = {}

        self.create_widgets()

    def create_widgets(self):
        # Movie Name Entry
        self.movie_name_label = tk.Label(self.master, text="Movie Name:")
        self.movie_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.movie_name_entry = tk.Entry(self.master)
        self.movie_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Rating Entry
        self.rating_label = tk.Label(self.master, text="Rating (1-5):")
        self.rating_label.grid(row=1, column=0, padx=10, pady=10)

        self.rating_scale = tk.Scale(self.master, from_=1, to=5, orient=tk.HORIZONTAL)
        self.rating_scale.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Rating", command=self.add_rating)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.average_button = tk.Button(self.master, text="Average Rating", command=self.show_average_rating)
        self.average_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(self.master, text="Display Ratings", command=self.display_ratings)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Bar Chart Canvas
        self.bar_chart_canvas = tk.Canvas(self.master, width=400, height=200)
        self.bar_chart_canvas.grid(row=5, column=0, columnspan=2, pady=10)

    def add_rating(self):
        movie_name = self.movie_name_entry.get()
        rating = self.rating_scale.get()

        if movie_name and 1 <= rating <= 5:
            if movie_name in self.movie_ratings:
                self.movie_ratings[movie_name].append(rating)
            else:
                self.movie_ratings[movie_name] = [rating]
            messagebox.showinfo("Success", f"Rating for {movie_name} added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a valid movie name and rating (1-5).")

    def show_average_rating(self):
        movie_name = self.movie_name_entry.get()
        if movie_name in self.movie_ratings and self.movie_ratings[movie_name]:
            average = sum(self.movie_ratings[movie_name]) / len(self.movie_ratings[movie_name])
            messagebox.showinfo("Average Rating", f"Average Rating for {movie_name}: {average:.2f}")
            self.plot_bar_chart(movie_name, average)
        else:
            messagebox.showinfo("Average Rating", f"No ratings available for {movie_name}.")

    def display_ratings(self):
        if not self.movie_ratings:
            messagebox.showinfo("Movie Ratings", "No ratings available.")
            return

        ratings_info = "Movie Ratings:\n"
        for movie_name, ratings in self.movie_ratings.items():
            average = sum(ratings) / len(ratings)
            ratings_info += f"{movie_name}: {ratings} - Average Rating: {average:.2f}\n"

        messagebox.showinfo("Movie Ratings", ratings_info)

    def plot_bar_chart(self, movie_name, average_rating):
        self.bar_chart_canvas.delete("all")  # Clear previous drawings

        star_width = 40
        star_height = 40

        full_stars = int(average_rating)
        remaining_star = average_rating - full_stars

        for i in range(full_stars):
            star_x = i * star_width
            self.draw_star(star_x, 0, star_width, star_height)

        if remaining_star > 0:
            partial_star_width = remaining_star * star_width
            self.draw_star(full_stars * star_width, 0, partial_star_width, star_height)

    def draw_star(self, x, y, width, height):
        star_points = [(0.5, 0), (0.61, 0.35), (1, 0.35), (0.68, 0.57), (0.79, 0.91), (0.5, 0.7),
                       (0.21, 0.91), (0.32, 0.57), (0, 0.35), (0.39, 0.35)]

        scaled_star_points = [(int((x + point[0] * width)), int((y + point[1] * height))) for point in star_points]

        self.bar_chart_canvas.create_polygon(scaled_star_points, fill="yellow", outline="black")

def main():
    root = tk.Tk()
    app = MovieRatingSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

