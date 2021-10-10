function normalizeTableHeights() {
    let maxHeight = Math.max($("#scott-col").height(), $("#kane-col").height());
    if ($(window).width() >= 768) {
        $("#scott-col").height(maxHeight);
        $("#kane-col").height(maxHeight);
    } else {
        $("#scott-col").height("fit-content");
        $("#kane-col").height("fit-content");
    }
}

window.addEventListener("load", normalizeTableHeights);
window.addEventListener("resize", normalizeTableHeights);