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

const toggleOnclick = (idToToggle, funcToToggle) => {
  document.getElementById(idToToggle).onclick = funcToToggle;
}

const select_tk_input = async (reqType, inType) => {
  // Removing the onclick function from the select path buttons to prevent the creation
  // of multiple file dialog windows (since the system is async, multiple windows will line up otherwise)
  if (reqType == "add") {
    toggleOnclick("new_filePathBtn", "");
    toggleOnclick("new_dirPathBtn", "");
  }

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
    
    // Returning the select_tk_input function to the select path buttons now that the 
    // dialogue window is closed.
    if (reqType == "add"){
      toggleOnclick("new_filePathBtn", () => select_tk_input(`add`,`file`));
      toggleOnclick("new_dirPathBtn", () => select_tk_input(`add`,`dir`));
    }

    return selected_path;
  }