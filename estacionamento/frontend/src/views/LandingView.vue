<template>
  <div class="d-flex fill-height" id="landing-view">
    <v-main style="background: #fff;">
      <v-row no-gutters class="py-6 d-flex content">
        <v-col 
          xl="2"
          lg="2"
          md="1"
          sm="0"
          xs="0"
        >
        </v-col>

        <v-col 
          xl="8"
          lg="8"
          md="10"
          sm="12"
          xs="12"
        >
          <v-row>
            <v-col 
              xl="6"
              lg="6"
              md="6"
              sm="12"
              xs="12"
              class="d-flex"
              :class="{'justify-center': !isXLarge && !isLarge && !isMedium}"
              >
              <!-- <div 
                class="banner-title"
              >
              </div> -->
                <v-img
                  aspect-ratio="16/9"
                  :src="require(`./../assets/clearfx.ai-black.png`)"
                  max-width="400"
                  style="height: 190px;"
                  contain
                  class="my-auto"
                >
                </v-img>

            </v-col>

            <v-col 
              xl="6"
              lg="6"
              md="6"
              sm="12"
              xs="12"
              class="d-flex"
              :class="{'justify-center': !isXLarge && !isLarge && !isMedium}"
            >
              <div 
                class="container-login d-flex flex-column justify-space-around"
              >
                <div class="d-flex flex-column">
                    <h2>{{ $t('landing.title') }}</h2>
                  <span>
                      <br>
                    {{ $t('landing.description.descriptionOne') }}
                    {{ $t('landing.description.descriptionTwo') }}
                  </span>

                  <!--
                  <span
                    class="mt-2 blue--text text-body-2 font-weight-light"
                    style="cursor: pointer;"
                  >
                    Learn More
                  </span>
                  -->

                  <v-btn 
                    color="primary"
                    elevation="0"
                    tile
                    class="mt-12"
                    style="
                    max-width: 65px !important;
                    min-width: 65px !important;
                    height: 40px;
                    "
                    href="/login"
                  >
                    <span class="text-capitalize font-weight-bold">
                      {{ $t('instructions.login') }}
                    </span>
                  </v-btn>
                </div>

                <!--
                <div class="text-body-2 font-weight-light">
                  Don't have access?  

                  <span
                    class="blue--text"
                    style="cursor: pointer;"
                  >
                    Register here
                  </span>
                </div>
                -->
              </div>
            </v-col>
          </v-row>
        </v-col>

        <v-col 
          xl="2"
          lg="2"
          md="1"
          sm="0"
          xs="0"
        >
        </v-col>
      </v-row>

      <v-row no-gutters class="py-4" style="background: #fff;">
        <v-col
          xl="2"
          lg="2"
          md="1"
          sm="0"
          xs="0"
        >
        </v-col>

        <v-col
          xl="8"
          lg="8"
          md="10"
          sm="12"
          xs="12"
        >
          <v-row>
            <v-col 
              xl="4"
              lg="4"
              md="4"
              sm="6"
              xs="12"
            >
              <v-card elevation="0" light :max-width="430">
                <v-card-title class="text-body-1 font-weight-bold">
                  {{ $t('landing.pricerConsole.title') }}
                </v-card-title>
                <v-card-text class="text-body-2 font-weight-light black--text">
                    {{ $t('landing.pricerConsole.descriptionOne') }}
                    {{ $t('landing.pricerConsole.descriptionTwo') }}
                    {{ $t('landing.pricerConsole.descriptionThree') }}
                </v-card-text>
                <v-card-actions class="px-4 py-0">
                  <!--
                  <span
                    class="text-caption font-weight-bold"
                    style="cursor: pointer;"
                  >
                    Learn More >>
                  </span>
                  -->
                </v-card-actions>
              </v-card>
            </v-col>

            <v-col 
              xl="4"
              lg="4"
              md="4"
              sm="6"
              xs="12"
            >
              <v-card elevation="0" light :max-width="430">
                <v-card-title class="text-body-1 font-weight-bold">
                  {{ $t('landing.deliverQuotes.title') }}
                </v-card-title>
                <v-card-text class="text-body-2 font-weight-light black--text">
                    {{ $t('landing.deliverQuotes.descriptionOne') }}
                    {{ $t('landing.deliverQuotes.descriptionTwo') }}
                    {{ $t('landing.deliverQuotes.descriptionThree') }}
                    {{ $t('landing.deliverQuotes.descriptionFour') }}
                </v-card-text>
                <v-card-actions class="px-4 py-0">
            <!--
                  <span
                    class="text-caption font-weight-bold"
                    style="cursor: pointer;"
                  >
                    Learn More >>
                  </span>
            -->
                </v-card-actions>
              </v-card>
            </v-col>

            <v-col
              xl="4"
              lg="4"
              md="4"
              sm="6"
              xs="12"
            >
              <v-card elevation="0" light :max-width="430">
                <v-card-title class="text-body-1 font-weight-bold">
                  {{ $t('landing.streamlineOperations.title') }}
                </v-card-title>
                <v-card-text class="text-body-2 font-weight-light black--text">
                    {{ $t('landing.streamlineOperations.descriptionOne') }}
                    {{ $t('landing.streamlineOperations.descriptionTwo') }}
                    {{ $t('landing.streamlineOperations.descriptionThree') }}
                    {{ $t('landing.streamlineOperations.descriptionFour') }}
                </v-card-text>
                <v-card-actions class="px-4 py-0">
            <!--
                  <span
                    class="text-caption font-weight-bold"
                    style="cursor: pointer;"
                  >
                    Learn More >>
                  </span>
            -->
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <v-footer light padless height="56" color="#fff" style="border-top: 1px solid #e1e1e1;">
        <v-row no-gutters>
          <v-col cols="2">
          </v-col>
          <v-col cols="8" class="d-flex text-caption">
            <div>
              {{ $t('extras.footer') }}
            </div>

            <v-spacer></v-spacer>

            <v-menu
              open-on-hover
              bottom
              offset-y
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  v-bind="attrs"
                  v-on="on"
                  plain
                >
                  <v-img
                    v-if="isPtBRLocale"
                    style="height: 32px;"
                    content-class="rounded-lg"
                    class="rounded-lg mr-2"
                    aspect-ratio="16/9"
                    max-width="32"
                    width="32"
                    :src="require(`./../assets/brazil_flag.png`)"
                  />
                  <v-img
                    v-else
                    style="height: 32px;"
                    content-class="rounded-lg"
                    class="rounded-lg mr-2"
                    aspect-ratio="16/9"
                    max-width="32"
                    width="32"
                    :src="require(`./../assets/usd_flag.png`)"
                  />
                  {{ $t('extras.language') }}
                  </v-btn>
              </template>

              <v-list style="background-color: white;">
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
                    <span style="color: #000" >EN-US</span>
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
                    <span style="color: #000" >PT-BR</span>
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <!--<div class="footer-menu"> Terms & Conditions </div>
            <v-divider vertical class="mx-6"></v-divider>
            <div class="footer-menu"> Privacy Policy </div>
            <v-divider vertical class="mx-6"></v-divider>
            <div class="footer-menu"> Contact Us </div>
            -->
          </v-col>
          <v-col cols="2">
          </v-col>
        </v-row>
      </v-footer>
    </v-main>
  </div>
</template>

<script>
import { useDisplayStore } from "./../store/index"
import { mapState } from "pinia"

export default {
  computed: {
    ...mapState(useDisplayStore, [
      "isXSmall",
      "isSmall",
      "isMedium",
      "isLarge",
      "isXLarge"
    ]),
    isPtBRLocale() {
      return this.$i18n.locale === "pt"
    },
  },
  methods: {
    changeLanguage(lang) {
      this.$i18n.locale = lang
      localStorage.setItem('userLanguage', lang)
    },
  }
}
</script>

<style scoped>
@font-face {
  font-family: AvenirNextCyr-Light;
  src: url("~@/assets/fonts/AvenirNextCyr-Light.ttf");
}
.content {
  background-image: url("./../assets/background-login.svg");
  background-repeat: repeat;
  background-color: #000;
  flex: 1 0 auto;
}
.banner-title {
  background-color: #000;
  color: #fff;
  font-size: 60px;
  font-weight: 500;
  letter-spacing: .29px;
  line-height: 73px;
  max-height: 200px;
  max-width: 520px;
  margin-top: 90px;
  padding: 25px 50px;
  text-align: center;
  word-wrap: break-word;
  display: flex;
}
.container-login {
  color: #fff;
  background-color: #000;
  /* margin-left: 13%; */
  max-width: 460px;
  font-size: 22px;
  text-align: start;
  max-height: 520px;
  height: 500px;
  font-weight: 300;
  padding: 0 10px 0 40px;
}
.footer-menu {
  cursor: pointer;
}
.footer-menu:hover {
  text-decoration: underline;
}
#landing-view .text-body-1,
#landing-view .text-body-2,
#landing-view .text-caption,
#landing-view {
  font-family: AvenirNextCyr-Light !important;
}
</style>

<!-- vim: set ts=4 sw=4 et: -->
