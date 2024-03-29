// =================================================================/
// FILL / MANIPULATE MODAL FUNCTIONS
// ===========================================================/ 

// ---------------------------------------------------------/
// ADD PROJECT MODAL
// ---------------------------------------------------/

// Object used by toggleWordGoal function to display the description of
// whichever goal the user has selected
const wcGoalDescription = {
    "weekly": "Input a target word goal for each day of the week manually. These will be your daily goals each week for the project's duration.",
    "daily": "Set a daily target word goal. This goal will be the same for each day for the duration of the project.",
    "total": "Set an overall target word goal for your project. Daily target word goals will be generated based on the number of days in the project and your overall goal"
}


// DOM manipulation function used by toggleWordGoal function to display
// the HTML fields of whichever word count goal the user has selected
const wordCountDivReturn = (wcGoalType) => {
    switch (wcGoalType){
        case "weekly":
            return `<table>
            <tbody>
                <tr>
                    <td><input class="wc-weekly-input" id="new_wc_mon" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_tues" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_wed" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_thurs" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_fri" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_sat" type="text" required></td>
                    <td><input class="wc-weekly-input" id="new_wc_sun" type="text" required></td>
                </tr>
                <tr>
                    <td class="wc-weekly-label">Mon</td>
                    <td class="wc-weekly-label">Tues</td>
                    <td class="wc-weekly-label">Wed</td>
                    <td class="wc-weekly-label">Thur</td>
                    <td class="wc-weekly-label">Fri</td>
                    <td class="wc-weekly-label">Sat</td>
                    <td class="wc-weekly-label">Sun</td>
                </tr>
            </tbody>
            </table>`
        case "daily":
            return `<input id="new_dailycountgoal" type="text" name="wordcountgoal" required> words`
        default:
            return `<input id="new_totalcountgoal" type="text" name="wordcountgoal" required> words`
    }
}

// CSS manipulation function used by toggleWordGoal function to switch
// the CSS classes of the word goal buttons to better reflect the user's
// selection
const toggleWordGoalClasses = (wcGoalType) => {
    let weeklyBtn = document.getElementById("new_wcWeeklyBtn");
    let dailyBtn = document.getElementById("new_wcDailyBtn");
    let totalBtn = document.getElementById("new_wcTotalBtn");

    switch (wcGoalType) {
        case "weekly":
            weeklyBtn.classList.add("selected-wc-btn");
            dailyBtn.classList.remove("selected-wc-btn");
            totalBtn.classList.remove("selected-wc-btn");
            break;
        case "daily":
            weeklyBtn.classList.remove("selected-wc-btn");
            dailyBtn.classList.add("selected-wc-btn");
            totalBtn.classList.remove("selected-wc-btn");
            break;
        default:
            weeklyBtn.classList.remove("selected-wc-btn");
            dailyBtn.classList.remove("selected-wc-btn");
            totalBtn.classList.add("selected-wc-btn");
    }
}


// Main class used to toggle between word goal form fields. 
// Uses above object / functions to add / replace form fields based on user choice.
// Toggled by the buttons themselves.
// wcGoalType is expected to be "daily", "weekly", or "total"; if it gets something weird
// it will assume the input to bee "total".
const toggleWordGoal = (wcGoalType) => {
    document.getElementById("new_wcGoalInterface").innerHTML = wordCountDivReturn(wcGoalType);
    document.getElementById("new_wcTypeDesc").innerHTML = wcGoalDescription[wcGoalType];

    toggleWordGoalClasses(wcGoalType);

    document.getElementById("new_wcSubmitBtn").innerHTML = `<button onclick="handleProjFormSubmit('new', '${wcGoalType}')">Create Project</button>`
}


// ---------------------------------------------------------/
// EDIT PROJECT MODAL
// ---------------------------------------------------/

// Sets up the edit project modal. The modal will appear differently based on the first variable (the word count goal type).
// Originally, this is called by the showEditModal function and then called again when daily / total buttons toggled.
const returnShowEditWordDivSection = (wcGoalType, weeklyGoals, dailyGoal, totalGoal, p_id) => {
    let wcDivSection = document.getElementById("edit_wcGoalInterface");

    switch (wcGoalType) {
        case "weekly":
            let rawWcGoals = weeklyGoals.split(",");
            wcDivSection.innerHTML = `<h5>Varied Daily Word Count Goals:</h5>
                <table>
                <tbody>
                    <tr>
                        <td><input class="wc-weekly-input" id="edit_wc_mon" type="text" value="${rawWcGoals[0]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_tues" type="text" value="${rawWcGoals[1]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_wed" type="text" value="${rawWcGoals[2]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_thurs" type="text" value="${rawWcGoals[3]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_fri" type="text" value="${rawWcGoals[4]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_sat" type="text" value="${rawWcGoals[5]}" required></td>
                        <td><input class="wc-weekly-input" id="edit_wc_sun" type="text" value="${rawWcGoals[6]}" required></td>
                    </tr>
                    <tr>
                        <td class="wc-weekly-label">Mon</td>
                        <td class="wc-weekly-label">Tues</td>
                        <td class="wc-weekly-label">Wed</td>
                        <td class="wc-weekly-label">Thur</td>
                        <td class="wc-weekly-label">Fri</td>
                        <td class="wc-weekly-label">Sat</td>
                        <td class="wc-weekly-label">Sun</td>
                    </tr>
                </tbody>
                </table>`
            break;
        case "daily":
            wcDivSection.innerHTML = `<div><button class="proj-form-btn" id="edit_wcDailyBtn" onclick="returnShowEditWordDivSection('daily', '${weeklyGoals}', '${dailyGoal}', '${totalGoal}', ${p_id})">Consistent Daily</button> 
            <button class="proj-form-btn selected-wc-btn" id="edit_wcTotalBtn" onclick="returnShowEditWordDivSection('total', '${weeklyGoals}', '${dailyGoal}', '${totalGoal}', ${p_id})">Overall</button></div>
            <h5>Consistent Daily Word Count Goal:</h5>
            <input id="edit_dailycountgoal" type="text" name="wordcountgoal" value="${dailyGoal}" required> words`
            break;
        default:
            wcDivSection.innerHTML = `<div><button class="proj-form-btn" id="edit_wcDailyBtn" onclick="returnShowEditWordDivSection('daily', '${weeklyGoals}', '${dailyGoal}', '${totalGoal}', ${p_id})">Consistent Daily</button> 
            <button class="proj-form-btn selected-wc-btn" id="edit_wcTotalBtn" onclick="returnShowEditWordDivSection('total', '${weeklyGoals}', '${dailyGoal}', '${totalGoal}', ${p_id})">Overall</button></div>
            <h5>Overall Word Count Goal:</h5>
            <input id="edit_totalcountgoal" type="text" name="wordcountgoal" value="${totalGoal}" required> words`
    }

    // Submit button includes the word count goal type since the function processing the input needs to know which
    // fields to look for
    document.getElementById("edit_wcSubmitBtn").innerHTML = `<button onclick="handleProjFormSubmit('edit', '${wcGoalType}', ${p_id})">Edit Project</button>`
}


// The main function for displaying the edit stats modal. Takes in the project id, gets the information required,
// and calls returnShowEditWordDivSection based on the wordtype
const showEditProjectModal = async(p_id) => {
    document.getElementById("edit-proj-toggle").click();
    
    let currProj = await eel.eel_get_proj_info(p_id)();

    // This part of the edit modal is the same regarless of word count goal type
    document.getElementById("edit_project-name").value = currProj.project_name;
    document.getElementById("edit_wcProjPath").innerHTML = currProj.project_path;
    document.getElementById("edit_targetstartdate").value = currProj.project_start_date;
    document.getElementById("edit_targetenddate").value = currProj.deadline;

    let wcGoalType = currProj.is_weekly_wordcount == 1 ? "weekly" : "total";
    returnShowEditWordDivSection(wcGoalType, currProj.weekly_words, currProj.current_daily_target, currProj.wordcount_goal, p_id);
}


// ---------------------------------------------------------/
// CSV EXPORT MODAL
// ---------------------------------------------------/

// Used to open and populate the CSV export screen for selected project
const showCSVExportModal = async(p_id ,errorNote="") => {
    document.getElementById("csv-exp-toggle").click();
    let projInfo = await eel.eel_get_proj_info(p_id)();
    let projName = projInfo.project_name;
    let errorDiv = errorNote != "" ? `<div id="csv_errorNote">${errorNote}</div>` : "";


    // Dynamically updating the title of modal so user knows which project they've selected
    document.getElementById("modal-csv-title").innerHTML = `Exporting ${projName}`
    
    // This section changes via JS whether the export is successful
    document.getElementById("csv-export-input").innerHTML = `<div id="csv-export-main" class="project-form new-project">
            ${errorDiv}
            <div>
                <h4>Where would you like your CSV uploaded?</h4>
                <button id="csv-export-request-btn" onclick="submitCSVExportRequest(${p_id})">Select Directory</button>
            </div>
        </div>`
}


// ---------------------------------------------------------/
// STATS MODAL
// ---------------------------------------------------/

// Used to open and populate the stats modal for the selected project
const showStatsModal = async (selectedId) => {
let selectedName =  document.querySelector('#project-' + String(selectedId) + '-summary h2').innerHTML;
let statsData = await eel.eel_return_project_stats(selectedId)();

document.getElementById("stats-toggle").click();
document.getElementById("modal-stats-title").innerHTML = `${selectedName} Statistics`

// This function can be found in stats-modal.js
statsModal_Populate(statsData);
}




// =================================================================/
// SUBMIT MODAL FUNCTIONS
// ===========================================================/ 

// ---------------------------------------------------------/
// ADD / EDIT PROJECT MODAL
// ---------------------------------------------------/

// This is the function run by the "Create Project" button.
// formType expected to be either "new" (add project) or "edit" (edit project)
// wcGoalType expected to be "daily", "weekly", or "total"
const handleProjFormSubmit = async (formType, wcGoalType, project_id=null) => {
    let allFilled = checkIfAnyEmpty(formType);
    if (allFilled) {
        let {authorname, projectname, projectpath, targetstartdate, targetenddate, wp_page, current_daily_target, 
            wordcountgoal, isWeekly, weeklyCount} = await projFormExtractVals(formType, wcGoalType);

        if (formType == "new") {
            eel.new_project(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath, isWeekly, weeklyCount);
            location.reload();
        } else {
            if (project_id != null) {
                eel.eel_update_project(wcGoalType, authorname, project_id, projectname, projectpath, 
                    targetstartdate, targetenddate, current_daily_target, wordcountgoal, isWeekly, weeklyCount)
                location.reload();
            }
            
        }
    } 
    else {
        alert("Please fill out all rows");
    } 
}

// Does exactly what you think it does. Runs on both the add project and edit project modals.
// Called by handleProjFormSubmit
const checkIfAnyEmpty = (formType) => {
    if (!document.getElementById(`${formType}_wcProjPath`).innerHTML) {
        return false;
    }

    let filledOut = true;

    document.getElementById(`${formType}-project`).querySelectorAll("[required]").forEach(i => {
        if (!filledOut){
            return false;
        } 
        if (!i.value) {
            filledOut = false;
        }
    })
    if (!filledOut) {
        return false;
    }
    return true;
}

// Called by handleFormSubmit once all fields have been filled out.
// Extracts all values from the form based on its modal (add or edit) and goal type (daily, weekly, total)
// Authorname currently defaulted to Author
const projFormExtractVals = async (formType, wcGoalType) => {
    let authorname = "Author";
    let projectname = document.getElementById(`${formType}_project-name`).value;
    let projectpath = document.getElementById(`${formType}_wcProjPath`).innerHTML;
    let targetstartdate = document.getElementById(`${formType}_targetstartdate`).value;
    let targetenddate = document.getElementById(`${formType}_targetenddate`).value;
    let wp_page = 42;
    let current_daily_target, wordcountgoal, isWeekly, weeklyCount;
    
    switch (wcGoalType){
        case "weekly":
            isWeekly = 1;
            let rawWcGoals = [];
            let suffix = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"];
            suffix.forEach(dotw => {
                rawWcGoals.push(document.getElementById(`${formType}_wc_${dotw}`).value);
            })
            weeklyCount = rawWcGoals.join(",");
            wordcountgoal = await eel.wcCalc_weeklyWordsCalc(weeklyCount, targetstartdate, targetenddate)();
            console.log(wordcountgoal);
            break;
        case "daily":
            isWeekly = 0;
            weeklyCount = "0,0,0,0,0,0,0";
            current_daily_target = document.getElementById(`${formType}_dailycountgoal`).value;
            wordcountgoal = await eel.wcCalc_wordgoalCalc(current_daily_target, targetstartdate, targetenddate, isWeekly)();
            break;
        default:
            isWeekly = 0;
            weeklyCount = "0,0,0,0,0,0,0";
            wordcountgoal = document.getElementById(`${formType}_totalcountgoal`).value;
            current_daily_target = await eel.wcCalc_dailyWordsCalc(wordcountgoal, targetstartdate, targetenddate)(); 
    }

    return {authorname:authorname, projectname: projectname, projectpath: projectpath, targetstartdate: targetstartdate, 
        targetenddate: targetenddate, wp_page:wp_page, current_daily_target: current_daily_target, 
        wordcountgoal: wordcountgoal, isWeekly:isWeekly, weeklyCount:weeklyCount}
}



// ---------------------------------------------------------/
// CSV EXPORT MODAL
// ---------------------------------------------------/

// Asks user for where they wish to export their CSV and tries to do so. Displays whether it was successful
// in the modal.
const submitCSVExportRequest = async (proj_id) => {
    toggleOnclick("csv-export-request-btn", "");

    let dir_path = String(await eel.dir_select_tk()())
    
    if (dir_path[dir_path.length - 1] != "/"){
      dir_path = dir_path + "/"
    }

    let export_success = await eel.eel_export_proj_to_csv(proj_id, dir_path)();
    
    let resp_message = export_success == 0 ? "" : "<p>There was an error in exporting your file. Please double-check the folder you've selected.</p>"; 

    if (export_success == 0) {
        // If file successfully exported, just reloads
        location.reload();
    } else {
        // If there was an error, brings back the CSV modal but with an error displayed
        showCSVExportModal(proj_id, resp_message);
    }
  }




// =================================================================/
// REFRESH WORDCOUNTS FOR VICTORY MODAL
// ===========================================================/ 
// Runs the typical refresh wordcounts function and displays the modal if
// the user met their goal
const refreshWordCountAndCheck = async (proj_id) => {
    let goalMet = await eel.eel_refresh_wordcounts(proj_id)();
    let projInfo = await eel.eel_get_proj_info(proj_id)();

    if (goalMet == true){
        document.getElementById("victory-modal-toggle").click();
        document.getElementById("victory-modal-container").innerHTML = `<h4>You just met your goal of ${projInfo.wordcount_goal} words!</h4>
            <p>If you'd like to write more, you can always edit your project goal!</p>`
    } else {
        location.reload();
    }
    
}