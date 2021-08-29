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





// =================================================================/
// OPEN / SUBMIT MODAL FUNCTIONS
// ===========================================================/ 

// ---------------------------------------------------------/
// ADD / EDIT PROJECT MODAL
// ---------------------------------------------------/

// This is the function run by the "Create Project" button.
// formType expected to be either "new" (add project) or "edit" (edit project)
// wcGoalType expected to be "daily", "weekly", or "total"
const handleProjFormSubmit = (formType, wcGoalType) => {
    let allFilled = checkIfAnyEmpty(formType);
    if (allFilled) {
        let {authorname, projectname, projectpath, targetstartdate, targetenddate, wp_page, current_daily_target, 
            wordcountgoal, isWeekly, weeklyCount} = projFormExtractVals(formType, wcGoalType);

        if (formType == "new") {
            console.log()
        }
    } 
    else {
        alert("Please fill out all rows");
    } 
}

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