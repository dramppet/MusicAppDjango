1.	Database
   •	Profile
       o	Username
           	Character field, required.
           	 It should have at least 2 characters and maximum - 15 characters.
           	The username can consist only of letters, numbers, and underscore ("_"). Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."
       o	Email
           	Email field, required.
       o	Age
           	Integer field, optional.
           	The age cannot be below 0.
   •	Album
       o	Album Name
           	Character field, required.
           	All album names must be unique.
           	 It should consist of a maximum of 30 characters.
       o	Artist
           	Character field, required.
           	It should consist of a maximum of 30 characters.
       o	Genre
           	Character field, required.
           	It should consist of a maximum of 30 characters.
           	The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
       o	Description
           	Text field, optional.
       o	Image URL
           	URL field, required.
       o	Price
           	Float field, required.
           	The price cannot be below 0.0.
       o	Owner
           	A foreign key to the Profile model.
           	Establishes a many-to-one relationship with the Profile model, associating each album with a profile.
           	The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
           	This field should remain hidden in forms.
2.	Routes
    •	http://localhost:8000/ - Home page
    •	http://localhost:8000/album/add/ - Add album page
    •	http://localhost:8000/album/<id>/details/- Details album page
    •	http://localhost:8000/album/<id>/edit/ - Edit album page
    •	http://localhost:8000/album/<id>/delete/ - Delete album page
    •	http://localhost:8000/profile/details/ - Profile details page
    •	http://localhost:8000/profile/delete/ - Delete profile page

