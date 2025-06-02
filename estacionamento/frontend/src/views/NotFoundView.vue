<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <h1>{{ $t('notFound.title') }}</h1>
        <p>
          {{ $t('notFound.descriptionOne') }}
          {{ $t('notFound.descriptionTwo') }}
          {{ $t('notFound.descriptionThree') }}
        </p>
        <p>{{ $t('notFound.apologies') }}</p>
        <v-btn color="primary" @click="goBack">{{ $t('instructions.back') }}</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'NotFoundView',
  methods: {
    goBack() {
      if (this.$route.path.startsWith('/techpark')) {
        this.$router.push('/techpark/home');
      } else {
        this.$router.push('/');
      }
    }
  }
}
</script>
