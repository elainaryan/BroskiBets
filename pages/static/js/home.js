function normalizeTableHeights() {
    let maxHeight = Math.max($("#scott-col").height(), $("#kane-col").height());
    console.log($(window).width());
    if ($(window).width() >= 768) {
        $("#scott-col").height(maxHeight);
        $("#kane-col").height(maxHeight);
    } else {
        $("#scott-col").height("fit-content");
        $("#kane-col").height("fit-content");
    }
}

function changeTitleColor() {
    $("#title").addClass("gradient");
    // $("#title").animate({backgroundColor: "green"}, 1500);
}

window.addEventListener("load", normalizeTableHeights);
window.addEventListener("resize", normalizeTableHeights);
window.addEventListener("load", changeTitleColor);