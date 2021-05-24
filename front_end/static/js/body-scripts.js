// Get and Display Username
window.onload = document.querySelectorAll('#username').forEach(x => x.textContent = get_username());

// Use Nantite as Given User
function username_given() {
username = document.querySelector('#username-in').value;
set_username(username) // set as current username
eel.new_author(username)(); // create author (or carry on if author exists)
window.location.href="http://localhost:8000/templates/projects.html";
}

function set_username(username) {
    document.cookie = 'username=' + encodeURIComponent(username) + '; expires=Thu, 18 Dec 2100 12:00:00 UTC';
}