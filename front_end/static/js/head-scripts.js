// Cookies Functions
function get_username() {
  return getCookie('username');
}

function getCookie(name) {
  // Split cookie string and get all individual name=value pairs in an array
  var cookieArr = document.cookie.split(";");
  
  // Loop through the array elements
  for(var i = 0; i < cookieArr.length; i++) {
      var cookiePair = cookieArr[i].split("=");
      
      /* Removing whitespace at the beginning of the cookie name
      and compare it with the given string */
      if(name == cookiePair[0].trim()) {
          // Decode the cookie value and return
          return decodeURIComponent(cookiePair[1]);
      }
  }
    // Return null if not found
    return null;
}

// Eel / Python Functions

async function dir_select_tk_input() {
    // Get the selected dir and put it into the input field
    let filepath_input = document.querySelector('.new-project input[name="filepath"]');
    // Call into Python to get file dialog box
    let selected_dir = await eel.dir_select_tk()();
    // Put it into the form input
    filepath_input.value = String(selected_dir);

    return selected_dir;
  }