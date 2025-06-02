<template>
  <iframe
    style="background: white;"
    :src="`${CLEARFXAI_API_URL}/apisandbox/redoc#/`"
    title="API Documentation"
    width="100%"
    :height="`${contentHeight-7}px`"
  >
  </iframe>
</template>

<script>
import { useDisplayStore, CLEARFXAI_API_URL } from "./../store/index"
import { mapState } from "pinia"

export default {
  data () {
    return {
      CLEARFXAI_API_URL: CLEARFXAI_API_URL
    }
  },
  computed: {
    ...mapState(useDisplayStore, [
      "isXSmall",
      "isSmall",
      "isMedium",
      "isLarge",
      "isXLarge",
      "contentHeight"
    ])
  }
}
</script>
