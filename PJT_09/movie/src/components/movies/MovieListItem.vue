<template>
  <div class="col-3 my-3">
    <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.id">
    <h3>{{ movie.name }}</h3>
    <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">
      영화 정보 상세보기
    </button>
      <movielistitemmodal :movie="movie" />
  </div>
</template>

<script>
import movielistitemmodal from './MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  components: {
    movielistitemmodal
  },
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
}
</script>

<style>
.movie--poster {
  width: 200px;
}
</style>