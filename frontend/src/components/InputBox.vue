<template>
  <input
    v-bind:value="value"
    v-on:input="$emit('input', $event.target.value)"
  />
</template>

<script>
export default {
  name: "InputBox",
  props: [
    "value"
  ],
}
</script>

<style>

</style>
