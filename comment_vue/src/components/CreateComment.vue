<template>
  <div class="create-comment">
    <button class="button is-primary" @click="showCommentInput = true">
      <span class="icon">
        <i class="fas fa-plus"></i>
      </span>
    </button>
    <div v-if="showCommentInput">
      <textarea class="textarea" v-model="newCommentText"></textarea>
      <button class="button is-success" @click="createComment">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: "CreateComment",
  data() {
    return {
      newCommentText: '',
      showCommentInput: false,
    }
  },
  methods: {
    async createComment() {
      try {
        const token = localStorage.getItem("token")

        const response = await axios.post("/comments/", {
          text: this.newCommentText,
        })

        const newComment = response.data

        this.$emit('comment-created', newComment);

        toast({
          message: 'Comment created successfully',
          type: 'is-success',
        })

        this.showCommentInput = false
        this.newCommentText = ''

        window.location.reload()
      } catch (error) {
        console.log(error)
        toast({
          message: 'Failed to create comment',
          type: 'is-danger',
        })
      }
    },
  }
}
</script>

<style>
</style>
