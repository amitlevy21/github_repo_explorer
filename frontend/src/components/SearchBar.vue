<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-autocomplete
          v-on:update:search-input="getOrganizationRepos"
          clearable
          dense
          rounded
          solo
          hide-no-data
        />
        <v-alert v-if="noRepoFound" type="error">No repositories found</v-alert>
        <v-list v-if="!noRepoFound">
          <v-card>
            <v-list-item v-for="(repo, i) in repos" :key="i">
              <v-list-item-content>
                <v-list-item-title v-text="repo"></v-list-item-title>
              </v-list-item-content> </v-list-item
          ></v-card>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      noRepoFound: true,
      repos: [],
      loading: true,
    };
  },
  methods: {
    getOrganizationRepos(search_input) {
      // TODO Rate limit this so the github API will not rate limit us
      axios
        .get(`http://localhost:5000/${search_input}`)
        .then((response) => {
          console.log(response);
          response.data.forEach((repo) => {
            this.repos.push(repo);
          });
          this.noRepoFound = false;
        })
        .catch(() => (this.noRepoFound = true));
    },
  },
};
</script>

<style scoped>
</style>