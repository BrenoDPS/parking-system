<template>
  <v-app-bar
    app
    :height="105"
    color="black"
  >
    <div
      style="width: 100%;"
      class="d-flex flex-column fill-height"
    >
      <div class="d-flex text-caption text--disabled font-weight-regular">
        {{ $t('toolbar.mesaCambio') }}
        <v-spacer></v-spacer>
        {{ $t('toolbar.timeZone') }}
      </div>

      <div class="my-auto d-flex">
        <v-img
          style="height: 65px;"
          aspect-ratio="16/9"
          :src="require(`./../assets/clearfx.ai-black.png`)"
          max-width="148"
          min-width="148"
          contain
          class="my-auto"
        >
        </v-img>

        <v-divider vertical class="mx-4"></v-divider>

        <div 
          class="my-auto font-weight-light text--secondary"
          style="font-size: 26px !important;"
        >
          {{ $t('toolbar.title') }}
        </div>

        <v-spacer></v-spacer>

        <v-menu
          open-on-hover
          bottom
          offset-y
        >
          <!-- <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="my-auto ml-12"
              v-bind="attrs"
              v-on="on"
              icon
            >
            <v-img
              v-if="isPtBRLocale"
              style="height: 32px;"
              content-class="rounded-lg"
              class="rounded-lg"
              aspect-ratio="16/9"
              max-width="32"
              width="32"
              :src="require(`./../assets/brazil_flag.png`)"
            />
            <v-img
              v-else
              style="height: 32px;"
              content-class="rounded-lg"
              class="rounded-lg"
              aspect-ratio="16/9"
              max-width="32"
              width="32"
              :src="require(`./../assets/usd_flag.png`)"
            />
            </v-btn>
          </template> -->

          <v-list>
            <v-list-item link @click="changeLanguage('en')">
              <v-img
                style="height: 32px;"
                content-class="rounded-lg"
                class="rounded-lg mr-2"
                aspect-ratio="16/9"
                max-width="32"
                width="32"
                :src="require(`./../assets/usd_flag.png`)"
              />
              <v-list-item-title>
                EN-US
              </v-list-item-title>
            </v-list-item>
            <v-list-item link @click="changeLanguage('pt')">
              <v-img
                style="height: 32px;"
                content-class="rounded-lg"
                class="rounded-lg mr-2"
                aspect-ratio="16/9"
                max-width="32"
                width="32"
                :src="require(`./../assets/brazil_flag.png`)"
              />
              <v-list-item-title>
                PT-BR
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>

        <v-menu
          open-on-hover
          bottom
          offset-y
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="ml-5"
              v-bind="attrs"
              v-on="on"
              icon
            >
              <v-icon>
                mdi-account
              </v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item link @click="logoutClicked()">
              <v-list-item-title>
                {{ $t('instructions.logout') }}
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </div>

    <template v-slot:extension>
      <v-tabs
        v-model="tab"
        dense
        background-color="#121212"
        :slider-size="5"
        :height="40"
        class="mt-3"
        style="border-bottom: 1px solid gray;"
      >
        <v-tab
          v-for="(menu, index) in menus"
          :key="index"
          :disabled="menu.disabled"
          :to="menu.to"
        >
          <span 
            class="white--text text-capitalize"
            style="font-weight: 400;"
          >
            {{ menu.label }}
          </span>
        </v-tab>
      </v-tabs>
    </template>

    <v-snackbar
      color="attention"
      v-model="logoutError"
    >
      {{ errorMessage }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="attention"
          text
          v-bind="attrs"
          @click="logoutError = false"
        >
          OK
        </v-btn>
      </template>
    </v-snackbar>
  </v-app-bar>
</template>

<script>
import { mapActions, mapWritableState } from "pinia";
import { useAuthStore } from "./../store/index";

export default {
  data () {
    return {
      tab: 0,
      logoutError: false,
      errorMessage: undefined,
    }
  },
  methods: {
    ...mapActions(useAuthStore, [
      "logout",
      "removeSessionLocalStorage"
    ]),
    logoutClicked () {
      this.authenticated = false
      this.userId = undefined
      this.removeSessionLocalStorage()
      this.$router.push("/")
      // this.logout()
      //   .then(() => {
      //     this.authenticated = false
      //     this.userId = undefined
      //     this.removeSessionLocalStorage()
      //     this.$router.push("/")
      //   })
      //   .catch((error) => {
      //     this.logoutError = true
      //     this.errorMessage = this.$t('toolbar.mesaCambio')
      //     console.log(error)
      //   })
    },
    changeLanguage(lang) {
      this.$i18n.locale = lang
      localStorage.setItem('userLanguage', lang)
      window.location.reload(true)
    },
  },
  computed: {
    ...mapWritableState(useAuthStore, [
      "authenticated",
      "userId"
    ]),
    isPtBRLocale() {
      return this.$i18n.locale === "pt"
    },
    menus() {
      return [
        { label: this.$t("menus.home"), to: "/techpark/home", disabled: false },
      ]
    },
  }
}
</script>

<style scoped>
::v-deep .v-toolbar__extension {
  height: 42px !important;
}
</style>
