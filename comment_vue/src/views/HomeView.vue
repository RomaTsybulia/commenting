<template>
  <div class="page-comment">
    <CreateComment @comment-created="addNewComment"/>
    <hr>
    <table class="table is-fullwidth">
      <tbody>
      <tr class="box" v-for="comment in comments" :key="comment.id">
        <div class="comment-head columns has-background-grey-light">
          <div class="main-information column is-11">
            {{ comment.author.logo }} {{ comment.author }} {{ comment.created_at }}
          </div>
          <ReplyComment :comment-id="comment.id" @reply-created="addNewReply"/>
          <DeleteComment
              :key="comment.id"
              :comment="comment"
              :current-user="currentUser"
              @delete="deleteComment"
          ></DeleteComment>
        </div>

        <div class="text">
          {{ comment.text }}
        </div>

        <div class="box" v-for="reply in comment.replies" :key="reply.id">
          <div class="reply columns">
            <div class="main-information column is-11 has-background-grey-light">
              {{ reply.author }} {{ reply.created_at }}
            </div>
            <EditComment :comment="comment" :currentUser="currentUser" />
            <ReplyComment :comment-id="comment.id" @reply-created="addNewReply"/>
          <DeleteComment
              :key="reply.id"
              :reply="reply"
              :current-user="currentUser"
              @delete="deleteComment"
          ></DeleteComment>
          </div>

          <div class="text">
            {{ reply.text }}
          </div>
        </div>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import CreateComment from '@/components/CreateComment.vue'
import ReplyComment from '@/components/CreateReply.vue'
import DeleteComment from "@/components/DeleteComment.vue"
import EditComment from "@/components/UpdateComment.vue"

export default {
  name: "Home",
  components: {
    CreateComment,
    ReplyComment,
    DeleteComment,
    EditComment
  },
  data() {
    return {
      comments: [],
    }
  },
  mounted() {
    this.fetchComments()
  },
  methods: {
    async fetchComments() {
      try {
        const response = await axios.get("/comments/")
        this.comments = response.data
      } catch (error) {
        console.log(error)
      }
    },
    addNewComment(comment) {
      this.comments.push(comment);
    },
    addNewReply(reply) {
      const commentIndex = this.comments.findIndex(
          (comment) => comment.id === reply.commentId
      );

      if (commentIndex !== -1) {
        this.comments[commentIndex].replies.push(reply);
      }
    },
  }
}
</script>

<style>
/* Add your custom styles here */
</style>
