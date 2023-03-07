module.exports = {
    darkMode: "class",
    mode: "jit",
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            width: {
                256: "36rem",
            },
            minWidth: {
                80: "20rem",
            },
            fontFamily: {
                sans: "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            },
            animation: {
                yellow2white: "yellow2white 1.5s linear",
            },
            keyframes: {
                yellow2white: {
                    "0%": { background: "rgba(255,255,150)" },
                    "100%": { background: "#fff" },
                },
            },
        },
    },
    plugins: [],
}
