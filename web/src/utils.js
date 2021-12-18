Date.prototype.getWeek = function () {
    var onejan = new Date(this.getFullYear(), 0, 1)
    return Math.ceil((((this - onejan) / 86400000) + onejan.getDay() + 1) / 7)
}

function fmt_date(d) {
    // Söndag v12 2021
    let weekdays = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]
    return weekdays[d.getDay()] + " v" + d.getWeek() + " " + d.getFullYear()
}
export {
    fmt_date
}