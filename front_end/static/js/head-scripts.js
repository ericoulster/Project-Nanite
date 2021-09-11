// Scripts at end of <head>
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

async function select_tk_input(reqType, inType) {
    // Call into Python to get file dialog box
    let selected_path = inType == "dir" ? await eel.dir_select_tk()() : await eel.file_select_tk()();
    // Display file path to user based on form
    switch(reqType){
      case "edit":
        // Currently not used as path cannot be edited
        document.getElementById("edit_wcProjPath").innerHTML = String(selected_path)
        break;
      default:
        // Default is for add project modal
        document.getElementById("new_wcProjPath").innerHTML = String(selected_path);
    }

    return selected_path;
  }