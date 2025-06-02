import { i18n } from "./plugins/vuetify"

export function padEnd2 (value) {
  if (!isNaN(value)) {
    const decimalPlaces = 2
    const padEndValue = "0"
    value = value.toString()
    let result = value.split(".")
    if (result[1] && result[1].length > decimalPlaces) {
      result[1] = result[1].substring(0, decimalPlaces)
      return result[0].concat(".").concat(result[1])
    }
    if (result[1]) {
      result[1] = result[1].padEnd(decimalPlaces, padEndValue)
      return result[0].concat(".").concat(result[1])
    }
    const decimals = "".padEnd(decimalPlaces, padEndValue)
    return value.concat(".").concat(decimals)
  }
  return value
}

export function padEnd4 (value) {
  if (isNaN(value)) {
    return value
  }
  const decimalPlaces = 4
  const padEndValue = "0"
  value = value.toString()
  let result = value.split(".")
  if (result[1] && result[1].length > decimalPlaces) {
    result[1] = result[1].substring(0, decimalPlaces)
    return result[0].concat(".").concat(result[1])
  }
  if (result[1]) {
    result[1] = result[1].padEnd(decimalPlaces, padEndValue)
    return result[0].concat(".").concat(result[1])
  }
  const decimals = "".padEnd(decimalPlaces, padEndValue)
  return value.concat(".").concat(decimals)
}

export function getPriceAndBips(price) {
  price = padEnd4(price);
  const priceSlited = price.split(".");
  const integer = priceSlited[0];
  let decimals = priceSlited[1];
  let sliceParameter = -2;
  const bips = decimals.slice(sliceParameter);
  decimals = decimals.slice(0, sliceParameter);
  price = `${integer}.${decimals}`;
  return { price: price, bips: bips };
}

export function getPriceAndBipsJPY(price) {
  price = padEndJpy(price)
  const priceSlited = price.split(".")
  const integer = priceSlited[0]
  let decimals = priceSlited[1]
  const sliceParameter = -4
  const bips = decimals.slice(sliceParameter)
  decimals = decimals.slice(0, sliceParameter)
  price = `${integer}.${decimals}`
  return { price: price, bips: bips }
}

export function getPriceAndBips2(price) {
  price = padEnd2(price);
  const priceSlited = price.split(".");
  const integer = priceSlited[0];
  let decimals = priceSlited[1];
  let sliceParameter = -2;
  const bips = decimals.slice(sliceParameter);
  decimals = decimals.slice(0, sliceParameter);
  price = `${integer}.${decimals}`;
  return { price: price, bips: bips };
}

export function padEndJpy (value) {
  if (!isNaN(value)) {
    const decimalPlaces = 6
    const padEndValue = "0"
    value = value.toString()
    let result = value.split(".")
    if (result[1]) {
      result[1] = result[1].padEnd(decimalPlaces, padEndValue)
      return result[0].concat(".").concat(result[1])
    }
    const decimals = "".padEnd(decimalPlaces, padEndValue)
    return value.concat(".").concat(decimals)
  }
  return value
}

export function formatPrice (price) {
  if (isNaN(price)) {
    return price
  }
  if (price === "") {
    return price
  }
  const priceStr = price.toString()
  const result = priceStr.split(".")
  if (result[1]) {
    let integer = result[0]
    const decimals = result[1]
    integer = integer.replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    return integer.concat(".").concat(decimals)
  }
  return priceStr.replace(/\B(?=(\d{3})+(?!\d))/g, ",").concat(".00")
}

export function getCurrentDateAndTime () {
  // Create a new Date object
  let currentDate = new Date();

  // Get the current date components
  let year = currentDate.getFullYear();
  let month = ('0' + (currentDate.getMonth() + 1)).slice(-2);
  let day = ('0' + currentDate.getDate()).slice(-2);

  // Get the current time components
  let hours = ('0' + currentDate.getHours()).slice(-2);
  let minutes = ('0' + currentDate.getMinutes()).slice(-2);
  let seconds = ('0' + currentDate.getSeconds()).slice(-2);

  // Create the formatted date and time string
  let formattedDateTime = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
  return formattedDateTime
}

export function getCurrentTime () {
  // Create a new Date object
  let currentDateNotification = new Date();

  // Get the current time components
  let hours = ('0' + currentDateNotification.getHours()).slice(-2);
  let minutes = ('0' + currentDateNotification.getMinutes()).slice(-2);
  let seconds = ('0' + currentDateNotification.getSeconds()).slice(-2);

  // Create the formatted date and time string
  let formattedDateTime = hours + ':' + minutes + ':' + seconds;
  return formattedDateTime
}

export function formatBRLPretty (price) {
  const ccy = "BRL"
  const intlNumberFormat = new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: ccy,
    currencyDisplay: "code"
	})
  price = intlNumberFormat.format(price)
  price = price.replace(ccy, "").trim()
  return price
}

export function formatUSDPretty (price) {
  if (!price) {
    return price
  }
  const ccy = "USD"
  const intlNumberFormat = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: ccy,
    currencyDisplay: "code"
	})
  price = intlNumberFormat.format(price)
  price = price.replace(ccy, "").trim()
  return price
}

export function getLocaleFormattedDateTime(timestamp) {
  let dateObject;

  if (!timestamp) {
    // Usado para a propriedade 'now' no componente, que chama a função sem timestamp.
    dateObject = new Date();
  } else if (typeof timestamp === 'string') {
    // Se o timestamp é uma string, new Date() geralmente lida bem com formatos ISO 8601.
    dateObject = new Date(timestamp);
  } else if (typeof timestamp === 'number') {
    // Se for um número, pode ser um timestamp UNIX.
    // Se estiver em segundos (ex: 1679602214), multiplique por 1000.
    // Se já estiver em milissegundos (ex: 1679602214000), use diretamente.
    // Uma heurística: timestamps em segundos são geralmente menores.
    if (timestamp < 3000000000) { // Supõe que abaixo deste valor está em segundos
        dateObject = new Date(timestamp * 1000);
    } else {
        dateObject = new Date(timestamp); // Supõe que já está em milissegundos
    }
  } else {
    console.warn('Formato de data/timestamp inesperado recebido:', timestamp);
    return 'Data Inválida (formato)'; // Retorno amigável
  }

  // Após tentar criar a data, verifique se é válida.
  if (!(dateObject instanceof Date) || isNaN(dateObject.getTime())) {
    console.warn('Timestamp resultou em Invalid Date na criação:', timestamp, 'Tentativa de objeto Date:', new Date(timestamp));
    return 'Data Inválida'; // Retorno amigável
  }

  let currentLocale;
  let atText;

  try {
    // Tenta usar a instância i18n importada.
    currentLocale = i18n.locale;
    atText = i18n.t('extras.at');
  } catch (e) {
    // Fallback caso i18n não esteja disponível ou configurado neste contexto.
    console.warn("Instância i18n não está acessível em utils.js. Usando fallbacks para formatação de data.", e);
    currentLocale = typeof navigator !== 'undefined' ? navigator.language : 'pt-BR'; // Tenta o idioma do navegador ou pt-BR.
    atText = (currentLocale && currentLocale.toLowerCase().startsWith('pt')) ? 'às' : 'at'; // Fallback simples para 'at'.
  }

  const dateOptions = {
    weekday: 'short',
    year: 'numeric',
    month: 'short',
    day: '2-digit',
  };

  const timeOptions = {
    hour: '2-digit',
    minute: '2-digit',
    // hour12 será definido abaixo com base no locale.
  };

  // Ajusta hour12: 'pt-BR' geralmente usa formato de 24h.
  if (currentLocale && currentLocale.toLowerCase().startsWith('pt')) {
    timeOptions.hour12 = false;
  } else {
    timeOptions.hour12 = true; // Padrão para outros locales.
  }

  const formattedDate = dateObject.toLocaleDateString(currentLocale, dateOptions);
  const formattedTime = dateObject.toLocaleTimeString(currentLocale, timeOptions);

  // Verificação final se a formatação resultou em "Invalid Date" (menos provável se a criação do dateObject foi bem-sucedida)
  if (formattedDate.toLowerCase().includes("invalid date") || formattedTime.toLowerCase().includes("invalid date")) {
      console.warn('Formatação resultou em Invalid Date:', {timestamp, dateObject, formattedDate, formattedTime});
      return 'Data Inválida (formatação)';
  }

  return `${formattedDate} ${atText} ${formattedTime}`;
}

export function getLocaleFormattedTime (timestamp) {
  let date = new Date()
  if (timestamp) {
    date = new Date(timestamp * 1000)
  }
  const time = date.toLocaleTimeString().split(" ") // ['9:21:53', 'PM']
  const period = time[1]
  const timeSplited = time[0].split(":")
  const hour = timeSplited[0]
  const minutes = timeSplited[1]
  return `${hour}:${minutes} ${period}`
}