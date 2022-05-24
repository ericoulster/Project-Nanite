// Checks whether Author is in the database and adds if not. Called by the welcome screen.
const prepNaniteUser = async() => {
    let currUsername = "Author";

    try {
        let is_in_db = await eel.get_author_id(currUsername)();
        console.log("Author already created");
        set_username('Author');
    } catch {
        console.log("Creating author")
        let creatingAuthor = await eel.new_author(currUsername)(); 
        set_username(currUsername);
        console.log("Successfully created!")
    }

    window.location.href="http://localhost:8000/templates/projects.html";

}
