<template>
    <div>
        <h1 class="my-4 font-bold text-center text-3xl">
            {{ top_n }} vanligaste lovsångerna
        </h1>
        <div
            class="
                flex flex-col flex-wrap
                sm:flex-row
                mt-5
                justify-center
            "
        >
            <div
                class="
                    sm:w-5/12
                    mx-2
                    my-2
                    rounded-lg
                    shadow-sm
                    border-2 border-gray-100
                    p-4
                    bg-blue-50
                    transition-colors
                    dark:bg-black dark:border-gray-800
                "
                v-for="year in years"
                :key="year"
            >
                <h2 class="font-bold text-center text-xl">
                    {{ year }}
                </h2>
                <canvas :id="'canvas_' + year"></canvas>
            </div>
        </div>
    </div>
</template>
<script>
import Chart from "chart.js/auto"
import { mapState, mapGetters } from "vuex"

function truncateString(str, num) {
    // If the length of str is less than or equal to num
    // just return str--don't truncate it.
    if (str.length <= num) {
        return str
    }
    // Return str truncated with '...' concatenated to the end of str.
    return str.slice(0, num) + "..."
}

export default {
    data() {
        return {
            top_n: 5,
        }
    },
    computed: {
        ...mapGetters(["playlists"]),
        ...mapState(["all_songs"]),
        years() {
            // list all years that exist in the database
            let years = this.playlists.map((p) =>
                p.playlist_date.getFullYear()
            )
            years.sort()

            // unique years
            return [...new Set(years)].reverse()
        },
    },
    methods: {
        value_counts(arr) {
            return arr.reduce(function (acc, curr) {
                return acc[curr] ? ++acc[curr] : (acc[curr] = 1), acc
            }, {})
        },
        data_most_common_by_year(year) {
            let this_year_sundays = this.playlists.filter(
                (p) => p.playlist_date.getFullYear() == year
            )
            let all_songs_from_playlists = this_year_sundays
                .map((a) => a.songs)
                .flat()

            let rm_single_slide_songs =
                all_songs_from_playlists.filter((song_title) => {
                    let song = this.all_songs.find(
                        (s) => s.title == song_title
                    )
                    if (song == null) return false

                    return song.text.length > 1
                })
            let counts = this.value_counts(rm_single_slide_songs)

            counts = Object.fromEntries(
                Object.entries(counts)
                    .sort(([, a], [, b]) => b - a)
                    .slice(0, this.top_n)
            )
            let data = Object.values(counts)
            let labels = Object.keys(counts).map((l) =>
                truncateString(l, 25)
            )

            let retval = {
                labels,
                datasets: [
                    {
                        label: year,
                        data,
                    },
                ],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                    "rgba(255, 205, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                ],
                borderColor: [
                    "rgb(255, 99, 132)",
                    "rgb(255, 159, 64)",
                    "rgb(255, 205, 86)",
                    "rgb(75, 192, 192)",
                    "rgb(54, 162, 235)",
                ],
                borderWidth: 1,
            }
            return retval
        },
    },
    mounted() {
        for (let year of this.years) {
            let ctx = document.getElementById("canvas_" + year)
            let data = this.data_most_common_by_year(year)

            new Chart(ctx, {
                type: "bar",
                data: data,
                options: {
                    plugins: {
                        legend: { display: false },
                    },
                    scales: {
                        y: {
                            ticks: { precision: 0 },
                            suggestedMin: 1,
                        },
                    },
                },
            })
        }
    },
}
</script>
