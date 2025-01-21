 Documentation: Movie Rating System 

 
 Overview

This project is a simple movie rating system built using Python's `tkinter` library. Users can rate movies, calculate their average ratings, and view all ratings. The application also visually represents the average rating using stars.

 Features

1. Add Rating: Allows users to add ratings (1-5) for a movie.
2. Show Average Rating: Calculates and displays the average rating for a specific movie.
3. Display All Ratings: Displays all movies with their respective ratings and average ratings.
4. Star Visualization: Visualizes the average rating as yellow stars.

Code Structure

The application consists of a class `MovieRatingSystemGUI` with the following methods:

1. __init__(self, master)

- Initializes the main GUI window and data structures.
- Calls `create_widgets()` to set up the interface.

2.create_widgets(self)

- Creates all GUI elements, including labels, text entry, buttons, and a canvas for visualization.
- Layout is organized using the `grid()` method.

 3. add_rating(self)

- Adds a rating for the specified movie.
- Validates input (movie name and rating between 1 and 5).
- Updates the `self.movie_ratings` dictionary with the new rating.
- Displays a success or error message using `messagebox`.

 4. show_average_rating(self)

- Calculates and displays the average rating for a specified movie.
- Shows a messagebox with the average rating.
- Calls `plot_bar_chart(movie_name, average)` to visualize the average rating with stars.

5. display_ratings(self)

- Displays all movies and their respective ratings in a messagebox.
- Shows the average rating for each movie.

 6. plot_bar_chart(self, movie_name, average_rating)

- Visualizes the average rating as yellow stars on the canvas.
- Clears any existing drawings before adding new ones.

7. draw_star(self, x, y, width, height)

- Draws a star at the specified position and size on the canvas.
- Uses a predefined set of star points to create the shape.

 Data Structure

- self.movie_ratings: A dictionary to store movie names as keys and a list of ratings as values.
  - Example: {"Inception": [5, 4, 3], "Titanic": [4, 5]}

 GUI Elements

 Labels

- Movie Name Label: Indicates the input field for the movie name.
- Rating Label: Indicates the rating slider for the user.

Entry

- Movie Name Entry: Accepts the name of the movie.

Scale

Rating Scale : Allows users to select a rating between 1 and 5.

Buttons

Add Rating : Adds a rating to the selected movie.
- Average Rating : Calculates and displays the average rating of a movie.
- Display Ratings : Displays all ratings and their averages.

 Canvas

- Used to display the star visualization for average ratings.

 How to Run

1. Ensure you have Python installed on your system.
2. Install `matplotlib` if not already installed:
      bash
   pip install matplotlib
   
3. Save the provided Python code to a file, e.g., `movie_rating_system.py`.
4. Run the file using the command:
   bash
   python movie_rating_system.py

Sample Usage

1. Enter a movie name in the text field.
2. Use the slider to select a rating between 1 and 5.
3. Click "Add Rating" to save the rating.
4. To view the average rating, re-enter the movie name and click "Average Rating."
5. To view all ratings, click "Display Ratings."
6. Observe the star visualization for average ratings below the buttons.

 Dependencies

- `tkinter`: For GUI components.
- `matplotlib`: For graphical visualization of ratings.

 Limitations

1. No persistence of data; all ratings are lost upon application exit.
2. Limited to integer ratings between 1 and 5.
3. Basic error handling.

 Future Improvements

1. Add functionality to save/load ratings from a file or database.
2. Enhance visualization with dynamic charting libraries.
3. Allow fractional ratings.
4. Improve UI design with advanced frameworks like `ttk` or `tkinter.ttk`.

 Conclusion

This application provides a simple and interactive way to rate movies and view average ratings. The GUI is beginner-friendly, and the use of visualization enhances user experience.

