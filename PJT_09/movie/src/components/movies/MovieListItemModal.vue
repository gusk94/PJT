<template>
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">{{ movie.name }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="text-center">
        <br>
        <img :src="movie.poster_url" class="w-50" :alt="movie.name">
      </div>
      <div class="modal-body">
        <hr>
        <p>{{ movie.rating }}</p>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'movie-list-item-modal',
  props: {
    movie: {
      type: Object,
      required: true
    }
  }
}
</script>

<style>

</style>