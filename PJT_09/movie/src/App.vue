<template>
  <div id="app">
    <div class="container">
      <movielist :movies="movies" :genres="genres" />
    </div>
  </div>
</template>

<script>
const axios = require('axios');
import movielist from "./components/movies/MovieList.vue"

export default {
  name: 'app',
  components: {
    movielist,
  },
  data() {
    return {
      movies: [],
      genres: [],
    }
  },
  methods: {
    getMovis: function(){
      axios.get("https://gist.githubusercontent.com/edujason-hphk/f57d4cb915fcec433ece535b2f08a10f/raw/612fd3f00468722ead2cfe809f14e38230b47686/movie.json")
        .then(response=>{
          this.movies = response.data
        })
    },
    getGenres: function(){
      axios.get("https://gist.githubusercontent.com/edujason-hphk/eea9c85a937cbf469b8f55fd7f8524df/raw/68bad38a2bc911d3a39bce26d6dd9b68a7efe849/genre.json")
        .then(response=>{
          this.genres = response.data
        })
    },
  },
  mounted() {
    this.getMovis()
    this.getGenres()
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
