module.exports = {
  darkMode: 'class',
  mode: 'jit',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      width: {
        '256': '36rem'
      },
      minWidth: {
        '80': '20rem',
      },
    },
  },
  plugins: [],
}