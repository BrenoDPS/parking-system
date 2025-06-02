<template>
  <v-expansion-panels 
    v-model="panel"
    class="help-window elevation-8 mr-2"
    accordion
    :style="{ 'max-width': panel === undefined ? '200px' : '750px' }"
  >
    <v-expansion-panel>
      <v-expansion-panel-header 
        hide-actions
        :color="panel === undefined ? 'alive' : 'black'"
        class="pa-1"
        style="height: 32px;"
      >
        <div class="d-flex align-center">
          <v-icon 
            class="mx-2"
            :color="panel === undefined ? 'grey darken-4' : 'alive'"
          >
            mdi-help-circle
          </v-icon>
          <span 
            :class="{
              'grey--text': panel === undefined, 
              'text--darken-4': panel === undefined,
              'white--text': panel !== undefined
            }"
          >
            {{ $t('requestHelp.requestHelp') }}
          </span>

          <v-spacer></v-spacer>

          <div class="mr-4">
            <v-btn 
              class="mr-4" 
              small 
              icon 
              v-if="panel !== undefined"
            >
              <v-icon>
                mdi-minus-thick
              </v-icon>
            </v-btn>

            <v-btn 
              class="mr-4"
              small
              icon
              disabled
              v-if="false"
            >
              <v-icon>
                mdi-arrow-expand
              </v-icon>
            </v-btn>
          </div>
        </div>
      </v-expansion-panel-header>
      <v-expansion-panel-content
        :style="{
          'max-height': isSmall || isXSmall || isMedium ? '400px' : '600px',
          'height': isSmall || isXSmall || isMedium ? '400px' : '600px'
        }"
      >
        <div style="overflow-y: auto; height: 100%;">          
          <div class="d-flex flex-column py-6 fill-height">
            <div class="text-h4">
              {{ $t('requestHelp.greeting') }}
            </div>

            <p>
              {{ $t('requestHelp.instruction') }}
            </p>

            <v-row>
              <v-col xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card 
                  outlined 
                  class="d-flex flex-column align-center justify-space-around"
                  :max-height="isSmall || isXSmall || isMedium ? 200 : 300"
                  :min-height="isSmall || isXSmall || isMedium ? 200 : 300"
                >
                  <v-icon :size="isSmall || isXSmall || isMedium ? 50 : 88">
                    mdi-email-outline
                  </v-icon>
                  
                  <div class="text-h6">
                    {{ $t('requestHelp.sendEmail.title') }}
                  </div>

                  <div>
                    <v-btn 
                      filled
                      tile
                      large
                      color="blue"
                      href="mailto:support@clearfxai.com"
                      target="_blank"
                    >
                      <span class="text-capitalize">
                        {{ $t('requestHelp.sendEmail.btnText') }}
                      </span>
                    </v-btn>
                  </div>
                </v-card>
              </v-col>

              <v-col xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card 
                  outlined 
                  class="d-flex flex-column align-center justify-space-around"
                  :max-height="isSmall || isXSmall || isMedium ? 200 : 300"
                  :min-height="isSmall || isXSmall || isMedium ? 200 : 300"
                >
                  <v-icon :size="isSmall || isXSmall || isMedium ? 50 : 88">
                    mdi-help-circle-outline
                  </v-icon>
                  
                  <div class="d-flex flex-column align-center">
                    <div class="text-h6">
                      {{ $t('requestHelp.helpTicket.title') }}
                    </div>
                    <div class="text-body-1">
                      {{ $t('requestHelp.helpTicket.description') }}
                    </div>
                  </div>
                  
                  <div>
                    <v-btn outlined tile large disabled>
                      <span class="text-capitalize">
                        {{ $t('requestHelp.helpTicket.btnText') }}
                      </span>
                    </v-btn>
                  </div>
                </v-card>
              </v-col>

              <v-col xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card 
                  outlined 
                  class="d-flex flex-column align-center justify-space-around"
                  :max-height="isSmall || isXSmall || isMedium ? 200 : 300"
                  :min-height="isSmall || isXSmall || isMedium ? 200 : 300"
                >
                  <v-icon :size="isSmall || isXSmall || isMedium ? 50 : 88">
                    mdi-chat-outline
                  </v-icon>
                  
                  <div class="text-h6">
                    {{ $t('requestHelp.liveChat.title') }}
                  </div>

                  <div>
                    <v-btn outlined tile large disabled>
                      <span class="text-capitalize">
                        {{ $t('requestHelp.liveChat.btnText') }}
                      </span>
                    </v-btn>
                  </div>
                </v-card>
              </v-col>
            </v-row>

            <div class="d-flex mt-auto">
              <v-spacer></v-spacer>
              <v-btn text @click="panel=undefined">
                <span class="text-capitalize">
                  {{ $t('instructions.close') }}
                </span>
              </v-btn>
            </div>
          </div>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>

export default {
  data () {
    return {
      panel: undefined
    }
  },
  props: {
    isXSmall: {
      type: Boolean,
      required: true
    },
    isSmall: {
      type: Boolean,
      required: true
    },
    isMedium: {
      type: Boolean,
      required: true
    },
    isLarge: {
      type: Boolean,
      required: true
    },
    isXLarge: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style scoped>
.help-window {
  position: fixed;
  right: 0px;
  bottom: 0px;
  z-index: 3;
  display: flex;
}
</style>