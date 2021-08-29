const wcGoalDescription = {
    "weekly": "Input a target word goal for each day of the week manually. These will be your daily goals each week for the project's duration.",
    "daily": "Set a daily target word goal. This goal will be the same for each day for the duration of the project.",
    "total": "Set an overall target word goal for your project. Daily target word goals will be generated based on the number of days in the project and your overall goal"
}

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

const toggleWordGoal = (wcGoalType) => {
    document.getElementById("new_wcGoalInterface").innerHTML = wordCountDivReturn(wcGoalType);
    document.getElementById("new_wcTypeDesc").innerHTML = wcGoalDescription[wcGoalType];

    toggleWordGoalClasses(wcGoalType);

    document.getElementById("new_wcSubmitBtn").innerHTML = `<button onclick="handleProjFormSubmit('new', '${wcGoalType}')">Create Project</button>`
}

const handleProjFormSubmit = (formType, wcGoalType) => {
    projFormExtractVals(formType, wcGoalType);
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

    console.log({authorname:authorname, projectname: projectname, projectpath: projectpath, targetstartdate: targetstartdate, 
        targetenddate: targetenddate, wp_page:wp_page, current_daily_target: current_daily_target, 
        wordcountgoal: wordcountgoal, isWeekly:isWeekly, weeklyCount:weeklyCount})
}
/*
*  <table>
            <tr>
                <td>Monday</td>
                <td><input id="new_wc_mon" type="text" required> words</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td><input id="new_wc_tues" type="text" required> words</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td><input id="new_wc_wed" type="text" required> words</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td><input id="new_wc_thurs" type="text" required> words</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td><input id="new_wc_fri" type="text" required> words</td>
            </tr>
            <tr>
                <td>Saturday</td>
                <td><input id="new_wc_sat" type="text" required> words</td>
            </tr>
            <tr>
                <td>Sunday</td>
                <td><input id="new_wc_sun" type="text" required> words</td>
            </tr>
        </table>
*/