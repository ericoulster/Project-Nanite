const wcGoalDescription = {
    "weekly": "Input a target word goal for each day of the week manually. These will be your daily goals each week for the project's duration.",
    "daily": "Set a daily target word goal. This goal will be the same for each day for the duration of the project.",
    "total": "Set an overall target word goal for your project. Daily target word goals will be generated based on the number of days in the project and your overall goal"
}

const wordCountDivReturn = (wcGoalType) => {
    switch (wcGoalType){
        case "weekly":
            return `<table>
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

    document.getElementById("new_wcSubmitBtn").innerHTML = `<button onclick="testExtractValues('${wcGoalType}')">Create Project</button>`
}