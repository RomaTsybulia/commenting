<template>
  <div class="create-comment">
    <button class="button is-primary" @click="showReplyInput = true">
      <span class="icon">
        <i class="fas fa-reply"></i>
      </span>
    </button>
    <div v-if="showReplyInput">
      <textarea class="textarea" v-model="newReplyText"></textarea>
      <button class="button is-success" @click="createReply">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: "CreateReply",
  props: {
    commentId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      newReplyText: '',
      showReplyInput: false,
    }
  },
  methods: {
    async createReply() {
      try {
        const token = localStorage.getItem("token")

        const response = await axios.post(`/comments/${this.commentId}/add_reply/`, {
          text: this.newReplyText,
        })

        const newReply = response.data

        this.$emit('reply-created', newReply);

        toast({
          message: 'Reply created successfully',
          type: 'is-success',
        })

        this.showReplyInput = false
        this.newReplyText = ''

        window.location.reload()
      } catch (error) {
        console.log(error)
        toast({
          message: 'Failed to create reply',
          type: 'is-danger',
        })
      }
    },
  }
}
</script>

<style>
/* Add your custom styles here */
</style>
