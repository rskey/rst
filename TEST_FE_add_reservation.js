const puppeteer = require('puppeteer'); // v23.0.0 or later

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const timeout = 5000;
    page.setDefaultTimeout(timeout);

    {
        const targetPage = page;
        await targetPage.setViewport({
            width: 1406,
            height: 1336
        })
    }
    {
        const targetPage = page;
        await targetPage.goto('https://dev-rtl.dq.skoda.vwg/dashboard');
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Search)'),
            targetPage.locator('#mat-input-193'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-193\\"])'),
            targetPage.locator(':scope >>> #mat-input-193')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 70.33331298828125,
                y: 6,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Search)'),
            targetPage.locator('#mat-input-193'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-193\\"])'),
            targetPage.locator(':scope >>> #mat-input-193')
        ])
            .setTimeout(timeout)
            .fill('testrack');
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Regress Testing - relays add autotest) >>>> ::-p-aria([role=\\"generic\\"])'),
            targetPage.locator('mat-panel-title'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-expansion-panel-header-48\\"]/span[1]/div/h2/mat-panel-title)'),
            targetPage.locator(':scope >>> mat-panel-title'),
            targetPage.locator('::-p-text(Regress Testing)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 174.33331298828125,
                y: 13.520828247070312,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Regress Testing - relays add autotest) >>>> ::-p-aria([role=\\"generic\\"])'),
            targetPage.locator('mat-panel-title'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-expansion-panel-header-48\\"]/span[1]/div/h2/mat-panel-title)'),
            targetPage.locator(':scope >>> mat-panel-title'),
            targetPage.locator('::-p-text(Regress Testing)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 174.33331298828125,
                y: 13.520828247070312,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('span.mat-content > div > div mat-icon'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-expansion-panel-header-48\\"]/span[1]/div/div/button/mat-icon)'),
            targetPage.locator(':scope >>> span.mat-content > div > div mat-icon'),
            targetPage.locator('::-p-text(edit)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 18,
                y: 15.333328247070312,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Test Benches[role=\\"heading\\"])'),
            targetPage.locator('#mat-tab-link-8 h2'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-tab-link-8\\"]/span[2]/span/h2)'),
            targetPage.locator(':scope >>> #mat-tab-link-8 h2')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 41.125,
                y: 16.25,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"rtl-link-nav-dashboard-page\\"]/span[2])'),
            targetPage.locator(':scope >>> #rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-text(DASHBOARD)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 24.354156494140625,
                y: 10.25,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Search)'),
            targetPage.locator('#mat-input-194'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-194\\"])'),
            targetPage.locator(':scope >>> #mat-input-194')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 141.33331298828125,
                y: 16,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Search)'),
            targetPage.locator('#mat-input-194'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-194\\"])'),
            targetPage.locator(':scope >>> #mat-input-194')
        ])
            .setTimeout(timeout)
            .fill('testing88');
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('div.connect-buttons div'),
            targetPage.locator('::-p-xpath(//*[@id=\\"cdk-accordion-child-70\\"]/div/div/testrack-list-item/mat-card/div[1]/div[5]/rtl-connect-button/div)'),
            targetPage.locator(':scope >>> div.connect-buttons div')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 71.33331298828125,
                y: 13,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('div.connect-buttons div'),
            targetPage.locator('::-p-xpath(//*[@id=\\"cdk-accordion-child-70\\"]/div/div/testrack-list-item/mat-card/div[1]/div[5]/rtl-connect-button/div)'),
            targetPage.locator(':scope >>> div.connect-buttons div')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 53.33331298828125,
                y: 13,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('div.testracks rtl-connect-button mat-icon'),
            targetPage.locator('::-p-xpath(//*[@id=\\"cdk-accordion-child-70\\"]/div/div/testrack-list-item/mat-card/div[1]/div[5]/rtl-connect-button/div/a[2]/button/mat-icon)'),
            targetPage.locator(':scope >>> div.testracks rtl-connect-button mat-icon')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 6.33331298828125,
                y: 6,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"rtl-link-nav-dashboard-page\\"]/span[2])'),
            targetPage.locator(':scope >>> #rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-text(DASHBOARD)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 61.354156494140625,
                y: 21.25,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#rtl-link-nav-reservation-page > span.mdc-button__label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"rtl-link-nav-reservation-page\\"]/span[2])'),
            targetPage.locator(':scope >>> #rtl-link-nav-reservation-page > span.mdc-button__label'),
            targetPage.locator('::-p-text(RESERVATIONS)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 55.83331298828125,
                y: 6.25,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(testing88) >>>> ::-p-aria([role=\\"generic\\"])'),
            targetPage.locator('mat-expansion-panel.ng-tns-c363401736-1348 a:nth-of-type(14) > div'),
            targetPage.locator('::-p-xpath(//*[@id=\\"cdk-accordion-child-98\\"]/div/div/a[14]/div)'),
            targetPage.locator(':scope >>> mat-expansion-panel.ng-tns-c363401736-1348 a:nth-of-type(14) > div'),
            targetPage.locator('::-p-text(testing88)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 30.333328247070312,
                y: 1.75,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('td:nth-of-type(2) tr:nth-of-type(25) > td'),
            targetPage.locator('::-p-xpath(/html/body/app-root/div/div[1]/app-reservation-system/div/div[2]/reservation-calendar/full-calendar/div[2]/div/table/tbody/tr/td[2]/div/div/div/div[1]/table/tbody/tr[25]/td)'),
            targetPage.locator(':scope >>> td:nth-of-type(2) tr:nth-of-type(25) > td')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 291,
                y: 1.0416259765625,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Title)'),
            targetPage.locator('#mat-input-196'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-196\\"])'),
            targetPage.locator(':scope >>> #mat-input-196')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 78.33331298828125,
                y: 12.33331298828125,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Title)'),
            targetPage.locator('#mat-input-196'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-input-196\\"])'),
            targetPage.locator(':scope >>> #mat-input-196')
        ])
            .setTimeout(timeout)
            .fill('testing FE reservation');
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('mat-form-field.ng-tns-c594611921-1381 mat-label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-mdc-form-field-label-402\\"]/mat-label)'),
            targetPage.locator(':scope >>> mat-form-field.ng-tns-c594611921-1381 mat-label'),
            targetPage.locator('::-p-text(Reservation Type)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 81.33331298828125,
                y: 2,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#mat-option-251 > span'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-option-251\\"]/span)'),
            targetPage.locator(':scope >>> #mat-option-251 > span'),
            targetPage.locator('::-p-text(Manual testing)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 65.33331298828125,
                y: 2.4166259765625,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('div.cdk-overlay-container button.mat-mdc-tooltip-trigger > span.mdc-button__label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"mat-mdc-dialog-0\\"]/div/div/app-reservation-dialog/div[2]/div[2]/button[2]/span[2])'),
            targetPage.locator(':scope >>> div.cdk-overlay-container button.mat-mdc-tooltip-trigger > span.mdc-button__label'),
            targetPage.locator('::-p-text(CONFIRM)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 21.625,
                y: 9.33331298828125,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"rtl-link-nav-dashboard-page\\"]/span[2])'),
            targetPage.locator(':scope >>> #rtl-link-nav-dashboard-page > span.mdc-button__label'),
            targetPage.locator('::-p-text(DASHBOARD)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 41.354156494140625,
                y: 5.25,
              },
            });
    }

    await browser.close();

})().catch(err => {
    console.error(err);
    process.exit(1);
});
