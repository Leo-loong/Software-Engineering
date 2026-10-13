const {By, Builder, Browser} = require('selenium-webdriver');
const assert = require("assert");

describe('First Selenium Test', function () {
  // 设置单个测试的最大超时时间（2分钟）
  this.timeout(120000);
  
  let driver;

  // 测试开始前自动启动Chrome浏览器
  before(async function () {
    driver = await new Builder().forBrowser(Browser.CHROME).build();
  });

  // 测试结束后自动关闭浏览器
  after(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it('should submit form and show Received!', async function () {
    // 1. 打开测试表单页面
    await driver.get('https://www.selenium.dev/selenium/web/web-form.html');

    // 2. 验证页面标题是否正确
    const pageTitle = await driver.getTitle();
    assert.strictEqual(pageTitle, 'Web form');

    // 3. 设置元素查找超时时间
    await driver.manage().setTimeouts({ implicit: 1000 });

    // 4. 找到文本输入框和提交按钮
    const textInput = await driver.findElement(By.name('my-text'));
    const submitBtn = await driver.findElement(By.css('button[type="submit"]'));

    // 5. 在输入框中输入文字
    await textInput.sendKeys('Selenium');

    // 6. 点击提交按钮
    await submitBtn.click();

    // 📸 非常重要：这里停留5秒，足够你截图
    await driver.sleep(5000);

    // 7. 验证提交成功的消息
    const successMessage = await driver.findElement(By.id('message'));
    const messageText = await successMessage.getText();
    assert.strictEqual(messageText, 'Received!');
  });
});
