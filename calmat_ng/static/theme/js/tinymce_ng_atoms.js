tinymce.init({
  selector: 'fieldset.tinymce-editable textarea',
  extended_valid_elements:'script[language|type|src]',
  height: 500,
  plugins: [
    'atoms advlist autolink lists link image imagetools charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table contextmenu paste code'
  ],
  // file_browser_callback: ImageLibraryBrowser,
  file_picker_callback: function(callback, value, meta) {
        ImageLibraryPicker(callback, value, meta);
  },
  contextmenu: "image atoms",
  toolbar: 'atoms insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  content_css: [
    '//fast.fonts.net/cssapi/e6dc9b99-64fe-4292-ad98-6974f93cd2a2.css',
    '//www.tinymce.com/css/codepen.min.css'
  ]
});