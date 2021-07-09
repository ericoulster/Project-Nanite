// TEMPORARY RESIZE PREVENTION FIX -- Need to research actual minimum screensize
// Adds an event listener to resize; checks current screen size; forces window to width > 533
window.addEventListener('resize', () => {
    let currWidth = window.innerWidth;

    // Responsivity breaks around 680, so if the screen is less than that--NO IT'S NOT
    if (currWidth < 680) {
        window.resizeTo(680, 900); // Height we don't care so much about so it can stay the same
    }
})