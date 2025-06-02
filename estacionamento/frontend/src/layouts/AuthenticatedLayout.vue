<template>
  <div>
    <tool-bar></tool-bar>

    <v-main>
      <router-view/>
    </v-main>

    <request-help-dialog
      :isXSmall="isXSmall"
      :isSmall="isSmall"
      :isMedium="isMedium"
      :isLarge="isLarge"
      :isXLarge="isXLarge"
    >
    </request-help-dialog>

    <!-- footer -->
  </div>
</template>

<script>
import RequestHelpDialog from "./../components/common/RequestHelpDialog.vue"
import { useDisplayStore, useAuthStore } from "./../store/index"
import { mapState, mapWritableState, mapActions } from "pinia"
import ToolBar from "./../components/ToolBar.vue"

export default {
  components: {
    RequestHelpDialog,
    ToolBar
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapWritableState(useAuthStore, [
      "authenticated",
      "userId"
    ]),
    ...mapState(useDisplayStore, [
      "isXSmall",
      "isSmall",
      "isMedium",
      "isLarge",
      "isXLarge"
    ]),
  },
  methods: {
    ...mapActions(useAuthStore, {
      getAuthenticated: "getAuthenticated",
      removeSessionLocalStorage: "removeSessionLocalStorage"
    }),
  },
  mounted () {
    const auth = Number(process.env.VUE_APP_AUTH)
    if (auth) {
      this.getAuthenticated()
        .then(() => {})
        .catch(() => {
          this.authenticated = false
          this.userId = undefined
          this.removeSessionLocalStorage()
          this.$router.push("/")
        })
    }
  }
}
</script>
