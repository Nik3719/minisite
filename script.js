const lengthInput = document.getElementById('length');
const lengthValue = document.getElementById('lengthValue');
const upperCheckbox = document.getElementById('upper');
const lowerCheckbox = document.getElementById('lower');
const numbersCheckbox = document.getElementById('numbers');
const symbolsCheckbox = document.getElementById('symbols');
const generateBtn = document.getElementById('generate');
const passwordField = document.getElementById('password');

const UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const LOWER = 'abcdefghijklmnopqrstuvwxyz';
const NUMBERS = '0123456789';
const SYMBOLS = '!@#$%^&*()_+-=[]{}|;:,.<>?';

lengthInput.addEventListener('input', () => {
  lengthValue.textContent = lengthInput.value;
});

generateBtn.addEventListener('click', () => {
  // Собираем набор символов
  let charset = '';
  if (upperCheckbox.checked)   charset += UPPER;
  if (lowerCheckbox.checked)   charset += LOWER;
  if (numbersCheckbox.checked) charset += NUMBERS;
  if (symbolsCheckbox.checked) charset += SYMBOLS;

  if (!charset) {
    passwordField.value = '';
    return;
  }

  const length = parseInt(lengthInput.value, 10);
  let pwd = '';

  // Безопасная генерация
  const values = new Uint32Array(length);
  window.crypto.getRandomValues(values);
  for (let i = 0; i < length; i++) {
    pwd += charset[values[i] % charset.length];
  }

  passwordField.value = pwd;
});