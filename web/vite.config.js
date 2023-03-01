const { createVuePlugin } = require('vite-plugin-vue2');
import WindiCSS from 'vite-plugin-windicss'


module.exports = {
  plugins: [createVuePlugin(), WindiCSS()],
};
