<template>
  <div>
    <div v-if="!editing">
      <button class="button is-primary" @click="startEditing">Edit</button>
    </div>
    <div v-else>
      <textarea class="textarea" v-model="updatedText"></textarea>
      <button class="button is-success" @click="saveChanges">Save</button>
      <button class="button is-danger" @click="cancelEditing">Cancel</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'EditComment',
  props: {
    comment: {
      type: Object,
      required: true
    },
    currentUser: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      editing: false,
      updatedText: ''
    };
  },
  methods: {
    startEditing() {
      this.editing = true;
      this.updatedText = this.comment.text;
    },
    saveChanges() {
      const updatedComment = { ...this.comment, text: this.updatedText };
       axios
    .put(`/api/comments/${updatedComment.id}/`, updatedComment)
    .then(() => {
      // Emit an event with the updated comment data
      this.$emit('comment-updated', updatedComment);
      this.editing = false;
    })
    .catch(error => {
      console.error('Error updating comment:', error);
      // Handle error if needed
    });
    },
    cancelEditing() {
      this.editing = false;
    }
  }
};
</script>
