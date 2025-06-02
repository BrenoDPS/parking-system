import axios from "axios";
import axiosRetry from "axios-retry";
// import { useUtilsStore } from "./store/index"

const axiosInstance = axios.create();

axiosRetry(axiosInstance, {
  retryDelay: (retryCount) => {
    retryCount;
    const miliseconds = 1000;
    const delayBetweenRetries = miliseconds; // retryCount * miliseconds
    return delayBetweenRetries;
  },
  retries: 0,
  retryCondition: (error) => {
    const response = error.response;
    if (response !== undefined && response !== null) {
      const status = response.status;
      if (status >= 400 && status < 500) {
        return false;
      }
    }
    // retry no matter what
    return true;
  },
});

// Add a request interceptor
axiosInstance.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
axiosInstance.interceptors.response.use(
  // Trigged if status code is 2xx
  // Do something with response data
  function (response) {
    return response;
  },
  // Trigged if status codes is not 2xx
  // Do something with response error
  function (error) {
    return Promise.reject(error);
  }
);

export default axiosInstance;
