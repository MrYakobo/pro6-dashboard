function fmt_date(d) {
    // Söndag v12 2021
    let weekdays = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    return weekdays[d.getDay()] + " v" + d.getWeek() + " " + d.getFullYear()
}
export {
    fmt_date
}