import { defineStore } from "pinia";
import axiosInstance from "@/http.js"; // Certifique-se que o caminho para http.js está correto
const axios = axiosInstance;

// Suas constantes globais de API
// (Se estas constantes não estiverem definidas neste arquivo,
// certifique-se de que elas estejam acessíveis ou importadas corretamente)
export const TECHPARK_API_URL = 'http://127.0.0.1:8000/api';
export const APIKEY = process.env.VUE_APP_APIKEY;
export const APIVERSION = process.env.VUE_APP_API_VERSION;
export const APP_PROD = process.env.VUE_APP_PROD;

export const API_PATH = `v${APIVERSION}/clearfxai`; // Exemplo, ajuste se não for usado pela usePlatesStore

export let AUTH_PATH = `apiauth/${API_PATH}`; // Usado pela useAuthStore
export let CONSOLE_AUTOPRICER_PATH = `consoleautopricer`; // Exemplo, ajuste se não for usado

// Store de Utilitários (sem alterações necessárias para esta funcionalidade)
export const useUtilsStore = defineStore("utils", {
  state: () => ({}),
  actions: {},
});

// Store de Placas (Modificada)
export const usePlatesStore = defineStore("plates", {
  state: () => ({
    registers: [], // Estado para armazenar a lista de registros
    users: [],     // Estado para armazenar a lista de usuários
    vehicles: [],  // Estado para armazenar a lista de veículos
    // Opcional: você pode adicionar estados de erro ou carregamento aqui também
    // error: null,
    // isLoadingRegisters: false,
    // isLoadingUsers: false,
    // isLoadingVehicles: false,
  }),
  actions: {
    async getRegisters() {
      // this.isLoadingRegisters = true; // Opcional: se quiser loading state na store
      try {
        const url = `${TECHPARK_API_URL}/registros/?format=json`;
        const response = await axios.get(url);
        // Assumindo que response.data é o array de registros.
        // Se sua API retornar os dados dentro de uma chave (ex: response.data.results),
        // ajuste para: this.registers = response.data.results;
        this.registers = response.data;
      } catch (error) {
        console.error("Erro ao buscar registros:", error);
        // this.error = error; // Opcional
        throw error; // Re-lança o erro para ser tratado no componente (ex: snackbar)
      } finally {
        // this.isLoadingRegisters = false; // Opcional
      }
    },
    async getUsers() {
      // this.isLoadingUsers = true; // Opcional
      try {
        const url = `${TECHPARK_API_URL}/usuarios/?format=json`;
        const response = await axios.get(url);
        // Assumindo que response.data é o array de usuários.
        // Ajuste se necessário (ex: this.users = response.data.results;)
        this.users = response.data;
      } catch (error) {
        console.error("Erro ao buscar usuários:", error);
        // this.error = error; // Opcional
        throw error;
      } finally {
        // this.isLoadingUsers = false; // Opcional
      }
    },
    async getVehicles() {
      // this.isLoadingVehicles = true; // Opcional
      try {
        const url = `${TECHPARK_API_URL}/veiculos/?format=json`;
        const response = await axios.get(url);
        // Assumindo que response.data é o array de veículos.
        // Ajuste se necessário (ex: this.vehicles = response.data.results;)
        this.vehicles = response.data;
      } catch (error) {
        console.error("Erro ao buscar veículos:", error);
        // this.error = error; // Opcional
        throw error;
      } finally {
        // this.isLoadingVehicles = false; // Opcional
      }
    }
  },
});

// Store de Autenticação (sem alterações necessárias para esta funcionalidade)
export const useAuthStore = defineStore("auth", {
  state: () => ({
    authenticated: undefined,
    userId: undefined,
    apiKey: undefined
  }),
  getters: {
    isAuthenticated: (state) => state.authenticated,
    getUserId: (state) => state.userId,
    getApiKey: (state) => state.apiKey,
  },
  actions: {
    login (payload) {
      const url = `${TECHPARK_API_URL}/${AUTH_PATH}/login`; // AUTH_PATH já inclui API_PATH
      return axios.post(url, payload);
    },
    getAuthenticated () {
      this.loadAuthenticatedAndUserIdStateFromLocalStorage();
      const userId = this.getUserId; // Use o getter
      const url = `${TECHPARK_API_URL}/${AUTH_PATH}/${userId}`;
      return axios.get(url);
    },
    logout () {
      const userId = this.getUserId; // Use o getter
      const url = `${TECHPARK_API_URL}/${AUTH_PATH}/logout/${userId}`;
      return axios.delete(url);
    },
    loadAuthenticatedAndUserIdStateFromLocalStorage () {
      let userId = localStorage.getItem("userId");
      let authenticated = false;
      if (userId) {
        authenticated = true;
      }
      this.authenticated = authenticated;
      this.userId = userId;
    },
    saveSessionLocalStorage (data) {
      localStorage.setItem("userId", data.user_id);
    },
    removeSessionLocalStorage () {
      localStorage.removeItem("userId");
      localStorage.removeItem("apiKey");
    },
    getSessionFromLocalStorage () {
      const data = localStorage.getItem("userId");
      return data;
    },
  },
});

// Store de Display (sem alterações necessárias para esta funcionalidade)
export const useDisplayStore = defineStore("display", {
  state: () => ({
    breakpoint: undefined,
    windowHeight: window.innerHeight,
    headerHeight: 153,
    // footerHeight: 30,
    marginLayout: 32,
  }),
  getters: {
    isMobile() { // Não há 'mobile' no state, talvez queira usar isXSmall ou isSmall
      return this.isXSmall || this.isSmall; // Exemplo de como poderia ser
    },
    currentBreakpoint (state) { // Adicionado 'state' para acesso direto
      return state.breakpoint;
    },
    isXLarge (state) {
      return state.breakpoint === "xl";
    },
    isLarge (state) {
      return state.breakpoint === "lg";
    },
    isMedium (state) {
      return state.breakpoint === "md";
    },
    isSmall (state) {
      return state.breakpoint === "sm";
    },
    isXSmall (state) {
      return state.breakpoint === "xs";
    },
    contentHeight (state) { // Adicionado 'state'
      const contentHeight =
        state.windowHeight
        - state.headerHeight
        // - state.footerHeight
        // - state.marginLayout // x axis
        // - state.marginLayout // y axis
      return `${contentHeight}`; // Retornar como número pode ser mais útil: return contentHeight;
    },
  },
  actions: {
    // Exemplo: ação para atualizar o breakpoint, se não estiver sendo feito de outra forma
    // setBreakpoint(vuetifyBreakpointObject) {
    //   this.breakpoint = vuetifyBreakpointObject.name; // 'name' é onde Vuetify guarda 'xs', 'sm', etc.
    //   this.windowHeight = vuetifyBreakpointObject.height; // Atualiza altura da janela se necessário
    // }
  }
});