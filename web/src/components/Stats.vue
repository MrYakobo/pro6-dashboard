<template>
    <div>
        <div class="flex flex-col sm:flex-row mt-5">
            <div class="sm:w-5/12" v-for="year in years" :key="year">
                <h1 class="font-bold text-center text-xl">
                    {{ top_n }} vanligaste lovsångerna {{ year }}
                </h1>
                <canvas :id="'canvas_' + year"></canvas>
            </div>
        </div>
    </div>
</template>
<script>
import Chart from 'chart.js/auto'
import { mapState, mapGetters } from 'vuex'

export default {
    data() {
        return {
            years: [2020, 2021],
            top_n: 5
        }
    },
    computed: {
        ...mapGetters(['sunday_playlists']),
        ...mapState(['all_songs'])
    },
    methods: {
        value_counts(arr) {
            return arr.reduce(function (acc, curr) {
                return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc
            }, {})
        },
        data_most_common_by_year(year) {
            let this_year_sundays = this.sunday_playlists.filter(p => p.playlist_date.getFullYear() == year)
            let all_songs_from_playlists = this_year_sundays.map(a => a.songs).flat()

            let remove_single_slides = all_songs_from_playlists.filter(song_title => {
                let song = this.all_songs.find(s => s.title == song_title)
                if (song == null)
                    return false

                let splitted = song.text.split(/(\n\s*){2,3}/)
                return splitted.length > 3
            })
            let counts = this.value_counts(remove_single_slides)


            counts = Object.fromEntries(
                Object.entries(counts).sort(([, a], [, b]) => b - a).slice(0, this.top_n)
            )
            let data = Object.values(counts)
            let labels = Object.keys(counts)


            let retval = {
                labels,
                datasets: [
                    {
                        label: year,
                        data
                    }
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                ],
                borderWidth: 1

            }
            return retval
        }
    },
    mounted() {
        for (let year of this.years) {
            console.log(year)
            let ctx = document.getElementById('canvas_' + year)
            let data = this.data_most_common_by_year(year)

            const chart = new Chart(ctx, {
                type: 'bar',
                data: data,
                options: {
                    scales: {
                        y: {
                            ticks: { precision: 0 },
                            suggestedMin: 1
                        }
                    },
                }
            })
        }
    }
}
</script>