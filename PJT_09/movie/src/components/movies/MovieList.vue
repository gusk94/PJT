<template>
  <div>
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <select class="form-control" v-model="genrename">
      <option>전체</option>
      <option v-for="genre in genres" v-bind:key="genre.id">{{genre.name}}</option>
    </select>
    <div class="row mt-5">
      <movielistitem v-for="movie in movieList" :movie="movie" :key="movie.id" />
    </div>
  </div>
</template>

<script>
import movielistitem from "./MovieListItem.vue";

export default {
  name: "MovieList",
  components: {
    movielistitem
  },
  data() {
    return {
      genrename: '',
    };
  },
  props: {
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    }
  },
  computed: {
    movieList: function() {
      if (this.genrename !== '' && this.genrename !== '전체'){
        const genre = this.genres.filter(genre => genre.name === this.genrename)
        return this.movies.filter(movie => movie.genre_id === genre[0].id)
      } else{
        return this.movies
      }
    }
  }
};
</script>

<style>
select {
  display: block;
  width: 50% !important;
  margin: 2rem auto !important;
}
</style>