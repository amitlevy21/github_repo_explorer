<template>
  <v-app>
    <v-app-bar app color="primary">
      <span class="mr-2">Latest Release</span>
    </v-app-bar>

    <v-main>
      <SearchBar />
    </v-main>
  </v-app>
</template>

<script>
import SearchBar from "./components/SearchBar";

export default {
  name: "App",

  components: {
    SearchBar,
  },

  data: () => ({
    //
  }),
};
</script>
