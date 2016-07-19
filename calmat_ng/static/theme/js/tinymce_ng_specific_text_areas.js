//  Todo:  Generalize this with the tiny_mce inits
//  Todo:  use this selector across full site, and configure what fields in admin
tinymce.init({
  selector: 'fieldset.tinymce-editable textarea',
  extended_valid_elements:'script[language|type|src]',
  height: 500,
  plugins: [
    'advlist autolink lists link image imagetools charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table contextmenu paste code'
  ],
  file_picker_callback: function(callback, value, meta) {
        ImageLibraryPicker(callback, value, meta);
  },
  contextmenu: "image",
  toolbar: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  content_css: [
    '//fast.fonts.net/cssapi/e6dc9b99-64fe-4292-ad98-6974f93cd2a2.css',
    '//www.tinymce.com/css/codepen.min.css'
  ]
});