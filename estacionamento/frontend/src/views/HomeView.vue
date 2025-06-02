<template>
  <div>
    <v-row no-gutters class="mb-8 px-8">
      <v-col xs="0" sm="0" md="0" lg="1" xl="1"></v-col>
      <v-col xs="12" sm="12" md="12" lg="10" xl="10" class="pt-8">
        <div class="d-flex flex-column">
          <div class="d-flex mb-8 pb-4 align-center">
            <div class="text-h3 font-weight-light">
              {{ $t('title.dashboardData') }}
            </div>
            <v-spacer></v-spacer>
            <div class="font-weight-light">
              {{ now }}
            </div>
          </div>

          <v-card class="mb-6">
            <v-card-title>
              <v-icon left>mdi-car</v-icon>
              {{ $t('pageTitles.vehicles') }}
            </v-card-title>
            <v-divider></v-divider>
            <v-data-table
              :headers="vehicleTableHeaders"
              :items="vehicles"
              item-key="id"
              class="elevation-1"
              :loading="loadingVehicles"
              :loading-text="$t('tables.loading')"
              :no-data-text="$t('tables.noData')"
              :footer-props="{
                'items-per-page-text': $t('tables.itemsPerPage'),
              }"
            >
              <template v-slot:[`item.data_cadastro`]="{ item }">
                <span>{{ item.data_cadastro | formatDate }}</span>
              </template>
            </v-data-table>
          </v-card>

          <v-card class="mb-6">
            <v-card-title>
              <v-icon left>mdi-account-group</v-icon>
              {{ $t('pageTitles.users') }}
            </v-card-title>
            <v-divider></v-divider>
            <v-data-table
              :headers="userTableHeaders"
              :items="users"
              item-key="id"
              class="elevation-1"
              :loading="loadingUsers"
              :loading-text="$t('tables.loading')"
              :no-data-text="$t('tables.noData')"
              :footer-props="{
                'items-per-page-text': $t('tables.itemsPerPage'),
              }"
            >
              <template v-slot:[`item.data_cadastro`]="{ item }">
                <span>{{ item.data_cadastro | formatDate }}</span>
              </template>
            </v-data-table>
          </v-card>

          <v-card class="mb-8">
            <v-card-title>
              <v-icon left>mdi-clipboard-list-outline</v-icon>
              {{ $t('pageTitles.accessRecords') }}
            </v-card-title>
            <v-divider></v-divider>
            <v-data-table
              :headers="registerTableHeaders"
              :items="registers"
              item-key="id"
              class="elevation-1"
              :loading="loadingRegisters"
              :loading-text="$t('tables.loading')"
              :no-data-text="$t('tables.noData')"
              :footer-props="{
                'items-per-page-text': $t('tables.itemsPerPage'),
              }"
            >
              <template v-slot:[`item.data_registro`]="{ item }">
                <span>{{ item.data_registro | formatDate }}</span>
              </template>
              <template v-slot:[`item.status`]="{ item }">
                <v-chip :color="getStatusColor(item.status)" dark small>
                  {{ getStatusText(item.status) }}
                </v-chip>
              </template>
            </v-data-table>
          </v-card>

        </div>
      </v-col>
      <v-col xs="0" sm="0" md="0" lg="1" xl="1"></v-col>
    </v-row>

    <v-snackbar
      v-model="snackbar.show"
      :color="snackbar.color"
      :timeout="snackbar.timeout"
      bottom
    >
      <span :class="snackbar.textColor || 'black--text'">
        {{ snackbar.message }}
      </span>
      <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="snackbar.show = false"
        >
          {{ $t('instructions.close') }}
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import { useDisplayStore, usePlatesStore } from "./../store/index"; // Ajuste o caminho se necessário
import { mapState, mapActions } from "pinia";
import * as utils from "./../utils.js"; // Ajuste o caminho se necessário

export default {
  components: {},
  filters: {
    formatDate(timestamp) {
      if (!timestamp) return '';
      return utils.getLocaleFormattedDateTime(timestamp);
    }
  },
  data() {
    return {
      snackbar: {
        show: false,
        message: '',
        color: 'green accent-4',
        timeout: 4000,
        textColor: 'black--text',
      },
      loadingVehicles: false,
      loadingUsers: false,
      loadingRegisters: false,
    };
  },
  computed: {
    ...mapState(useDisplayStore, [
      "isXSmall",
      "isSmall",
      "isMedium",
      "isLarge",
      "isXLarge"
    ]),
    ...mapState(usePlatesStore, [
      "vehicles",
      "users",
      "registers"
    ]),
    now() {
      return utils.getLocaleFormattedDateTime();
    },
    vehicleTableHeaders() {
      return [
        { text: this.$t('headers.vehicles.plate'), value: 'placa' },
        { text: this.$t('headers.vehicles.brand'), value: 'marca' },
        { text: this.$t('headers.vehicles.model'), value: 'modelo' },
        { text: this.$t('headers.vehicles.color'), value: 'cor' },
        { text: this.$t('headers.vehicles.userName'), value: 'usuario_nome' },
        { text: this.$t('headers.vehicles.userRegistry'), value: 'usuario_matricula' },
        { text: this.$t('headers.vehicles.registrationDate'), value: 'data_cadastro' },
      ];
    },
    userTableHeaders() {
      return [
        { text: this.$t('headers.users.name'), value: 'nome' },
        { text: this.$t('headers.users.registry'), value: 'matricula' },
        { text: this.$t('headers.users.email'), value: 'email' },
        { text: this.$t('headers.users.phone'), value: 'telefone' },
        { text: this.$t('headers.users.type'), value: 'tipo_usuario' },
        { text: this.$t('headers.users.courseDepartment'), value: 'curso' },
        { text: this.$t('headers.users.registrationDate'), value: 'data_cadastro' },
      ];
    },
    registerTableHeaders() {
      return [
        { text: this.$t('headers.registers.vehiclePlate'), value: 'veiculo_placa' },
        { text: this.$t('headers.registers.recognizedPlate'), value: 'placa_reconhecida' },
        { text: this.$t('headers.registers.userName'), value: 'usuario_nome' },
        { text: this.$t('headers.registers.userRegistry'), value: 'usuario_matricula' },
        { text: this.$t('headers.registers.dateTime'), value: 'data_registro' },
        { text: this.$t('headers.registers.status'), value: 'status' },
      ];
    }
  },
  async mounted() {
    this.loadingVehicles = true;
    this.loadingUsers = true;
    this.loadingRegisters = true;

    try {
      // Usando os nomes das actions diretamente como mapeadas
      await Promise.all([
        this.getVehicles(),
        this.getUsers(),
        this.getRegisters()
      ]);
      // Exemplo de notificação de sucesso (se necessário após o fetch, embora o snackbar original fosse para 'updatedSucces')
      // this.showSnackbar(this.$t('fxEngine.spreads.edit.updatedSucces')); // Ajuste a mensagem conforme o contexto
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
      this.showSnackbar(this.$t('notifications.fetchDataError'), 'red accent-4', 'white--text');
    } finally {
      this.loadingVehicles = false;
      this.loadingUsers = false;
      this.loadingRegisters = false;
    }
  },
  methods: {
    ...mapActions(usePlatesStore, [
      "getVehicles",
      "getUsers",
      "getRegisters"
    ]),
    showSnackbar(message, color = 'green accent-4', textColor = 'black--text', timeout = 4000) {
      this.snackbar.message = message;
      this.snackbar.color = color;
      this.snackbar.textColor = textColor;
      this.snackbar.timeout = timeout;
      this.snackbar.show = true;
    },
    getStatusColor(status) {
      if (!status) return 'grey';
      const lowerStatus = status.toLowerCase();
      if (lowerStatus === 'entrada' || lowerStatus === 'entry') return 'blue accent-3';
      if (lowerStatus === 'saída' || lowerStatus === 'exit') return 'orange darken-2';
      return 'grey';
    },
    getStatusText(status) {
      if (!status) return status;
      const lowerStatus = status.toLowerCase();
      if (lowerStatus === 'entrada' || lowerStatus === 'entry') return this.$t('statusTypes.entry');
      if (lowerStatus === 'saída' || lowerStatus === 'exit') return this.$t('statusTypes.exit');
      return status;
    }
  }
};
</script>

<style scoped>
/* Adicione estilos personalizados aqui se necessário */
.v-card + .v-card {
  margin-top: 24px;
}
</style>