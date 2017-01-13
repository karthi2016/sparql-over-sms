<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              <h3>Message Details</h3>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <div class="form-group">
                <label for="exampleTextarea">Content</label>
                <textarea class="form-control" id="exampleTextarea" rows="10" v-model="message.body" disabled></textarea>
              </div>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn" @click="close">Close</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    props: ['message'],

    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';
</style>
