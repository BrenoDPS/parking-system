import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import colors from "vuetify/lib/util/colors"
import i18n from "./../i18n/i18n.js";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    dark: true,
    themes: {
      light: {
        primary: "#007BFF",
        secondary: "#424242",
        accent: "#82B1FF",
        error: "#FF5252",
        info: "#2196F3",
        success: "#4CAF50",
        warning: "#FFC107",
      },
      dark: {
        base: colors.grey.darken4, // "#1c0021",
        secondary: colors.blue.lighten1, // colors.grey.darken2, // colors.lightBlue.darken2, //  "#00a9d4",
        accent: colors.orange.base,// "#40ffdc",
        attention: "#ED2B2A", // #ff5260 colors.red.accent3,
        alive: colors.green.accent4, // accent3
        primary: "#0073ff"
      }
    },
  },
  lang: {
    t: (key, ...params) => i18n.t(key, params),
  },
});

export { i18n };