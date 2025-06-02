<template>
  <v-app v-resize="updateWindowHeight">
    <router-view/>
  </v-app>
</template>

<script>
import { mapState, mapWritableState } from "pinia"
import { useDisplayStore } from "./store/index"

export default {
  watch: {
    breakpoint: {
      handler (newValue) {
        this.setBreakpoint(newValue)
      }
    },
  },
  mounted () {
    this.setBreakpoint(this.breakpoint)
  },
  data () {
    return {
      tab: 0,
      menus: [
        { label: "Home", to: "/home" }
        //{ label: "API Documentation", to: "/api-doc", disabled: true  },
        //{ label: "API Test in-place", to: "/api-sandbox", disabled: true  },
        //{ label: "Monitoring (TBR)", disabled: true },
        //{ label: "IP Allowlist (TBR)", disabled: true },
        //{ label: "Session (TBR)", disabled: true },
        //{ label: "Notifications (TBR)", disabled: true }
      ],
      panel: undefined
    }
  },
  computed: {
    ...mapWritableState(useDisplayStore, {
      breakpointState: "breakpoint",
      windowHeightState: "windowHeight",
    }),
    ...mapState(useDisplayStore, [
      "isXSmall",
      "isSmall",
      "isMedium",
      "isLarge",
      "isXLarge"
    ]),
    breakpoint () {
      return this.$vuetify.breakpoint.name
    }
  },
  methods: {
    setBreakpoint (value) {
      this.breakpointState = value
    },
    updateWindowHeight () {
      this.windowHeightState = window.innerHeight
    },
  }
}
</script>

<style scoped>
@font-face {
  font-family: AvenirNextM-Regular;
  src: url("~@/assets/fonts/AvenirNextM-Regular.ttf");
}
</style>
