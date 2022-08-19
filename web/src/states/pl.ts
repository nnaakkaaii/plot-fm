import { atom } from 'recoil';

interface PLRow {
    fy: number,
    attr: string,
    price: number,
}

interface PL {
    company_id: string,
    company_name: string,
    data: PLRow[],
}

const plState = atom<PL>({
    key: 'plState',
    default: undefined,
});

export default plState;