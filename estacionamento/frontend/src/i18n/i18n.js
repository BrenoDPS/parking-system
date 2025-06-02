import Vue from "vue";
import VueI18n from "vue-i18n";
import en from "vuetify/lib/locale/en";
import pt from "vuetify/lib/locale/pt";
import enMessages from './locales/en.json'
import ptMessages from './locales/pt.json'

Vue.use(VueI18n);

const messages = {
  en: {
    $vuetify: en,
    ...enMessages
  },
  pt: {
    $vuetify: pt,
    ...ptMessages
  }
};
    
const initialLocale = localStorage.getItem('userLanguage') || 'pt';

const i18n = new VueI18n({
  locale: initialLocale,
  fallbackLocale: 'pt',
  messages,
});

export default i18n;
