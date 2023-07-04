<template>
  <button class="button is-danger" @click="deleteComment">
    <span class="icon">
      <i class="fas fa-trash"></i>
    </span>
  </button>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: 'DeleteComment',
  props: {
    comment: {
      type: Object,
      required: true
    },
  },
  methods: {
    deleteComment() {
      if (this.comment.author === localStorage.getItem("user")) {
        axios
          .delete(`/comments/${this.comment.id}/`)
          .then(response => {
            this.$emit('delete', this.comment);
            toast({
              message: 'Comment deleted successfully',
              type: 'is-success'
            });
            window.location.reload()
          })
          .catch(error => {
            // Handle error, e.g., show an error message
            toast({
              message: 'Failed to delete comment',
              type: 'is-danger'
            });
          });
      } else {
        toast({
          message: 'You are not authorized to delete this comment',
          type: 'is-danger'
        });
      }
    }
  }
};
</script>
